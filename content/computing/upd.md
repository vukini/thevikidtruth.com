---
title: Updating the Database
date: '2016-11-26T21:10:03+04:00'
lastmod: '2016-11-26T21:27:20+04:00'
original_id: '{A374}'
original_name: upd
original_blob: blob/B/2/214.txt
revisions: 5
author: admin
last_editor: admin
tags:
- computing
categories:
- computing
wikislug: upd
draft: true
review: update
topics:
- lisp
---

# Updating the Database

[ASM](pilasm.md) | [Picolisp](picolisp.md) | [Computing](computing.md)

**upd is the default syncronization function**

**(upd sym ..) -> lst**

Synchronizes the internal state of all passed (external) symbols by passing them to wipe.
upd is the standard function passed to commit during database transactions.

**(commit 'upd)**  # Commit changes, informing all sister processes

**(wipe 'sym|lst) -> sym|lst**

- Clears the VAL and the property list of sym, or of all symbols in the list lst.
- When a symbol is an external symbol, its state is also set to "not loaded".
- Does nothing when sym is an external symbol that has been modified or deleted ("dirty").

```
: (setq A (1 2 3 4))
-> (1 2 3 4)
: (put 'A 'a 1)
-> 1
: (put 'A 'b 2)
-> 2
: (show 'A)
A (1 2 3 4)
   b 2
   a 1
-> A
: (wipe 'A)
-> A
: (show 'A)
A NIL
-> A
```

## Definitions

```
(de upd Lst
  (wipe Lst) )
```

```
# (wipe 'sym|lst) -> sym|lst
(code 'doWipe 2)
   push X
   ld X E
   ld E ((E CDR))  # Get arg
   eval  # Eval it
   cmp E Nil  # NIL?
   if ne  # No
      atom E  # List?
      if nz  # No
         call wipeEX  # Wipe it
      else
         push E  # Save
         ld C E  # Get list
         do
            ld E (C)  # Next symbol
            call wipeEX  # Wipe it
            ld C (C CDR)
            atom C  # More?
         until nz  # No
         pop E
      end
   end
   pop X
   ret
```

```
# (commit ['any] [exe1] [exe2]) -> T
(code 'doCommit 2)
   push X
   push Y
   push Z
   ld X E
   ld Y (E CDR)  # Y on args
   ld E (Y)  # Eval 'any'
   eval
   link
   push E  # <L I> 'any'
   link
   null (DbLog)  # Transaction log?
   if z  # No
      inc (EnvProtect)  # Protect the operation
   end
   call wrLockDb  # Write lock DB
   null (DbJnl)  # Journal?
   if nz  # Yes
      call lockJnl  # Write lock journal
   end
   null (DbLog)  # Transaction log?
   if nz  # Yes
      ld E (DbFiles)  # Iterate DB files
      ld C (DBs)  # Count
      do
         set (E (+ IV 1)) 0  # Clear dirty flag
         ld (E VII) 0  # and 'fluse'
         add E VIII  # Increment by sizeof(dbFile)
         sub C VIII  # Done?
      until z  # Yes
      push X
      push Y
      ld X (Extern)  # Iterate external symbol tree
      ld Y 0  # Clear TOS
      do
         do
            ld A (X CDR)  # Get subtrees
            atom (A)  # Left subtree?
         while z  # Yes
            ld C X  # Go left
            ld X (A)  # Invert tree
            ld (A) Y  # TOS
            ld Y C
         loop
         do
            ld A ((X) TAIL)  # Get external symbol's tail
            call nameA_A  # Get name
            rxl A 1  # Dirty or deleted?
            if x  # Yes
               push Y
               rxr A 1
               ld Y A  # Name in Y
               call dbFileBlkY_AC  # Get file and block index
               cmp A (DBs)  # Local file?
               if lt  # Yes
                  call setBlockAC_Z  # Set up block env
                  call rdBlockZ_Z  # Read first block
                  do
                     call logBlock  # Write to transaction log
                     null (BlkLink)  # More blocks?
                  while nz  # Yes
                     call rdBlockLinkZ_Z  # Read next block
                  loop
                  ld C (DbFile)
                  set (C (+ IV 1)) 1  # Set dirty flag
                  rxl Y 2  # Deleted?
                  if nx  # No
                     inc (C VII)  # Increment 'fluse'
                  end
               end
               pop Y
            end
            ld A (X CDR)  # Right subtree?
            atom (A CDR)
            if z  # Yes
               ld C X  # Go right
               ld X (A CDR)  # Invert tree
               ld (A CDR) Y  # TOS
               or C SYM  # First visit
               ld Y C
               break T
            end
            do
               ld A Y  # TOS
               null A  # Empty?
               jeq 20  # Done
               sym A  # Second visit?
               if z  # Yes
                  ld C (A CDR)  # Nodes
                  ld Y (C)  # TOS on up link
                  ld (C) X
                  ld X A
                  break T
               end
               off A SYM  # Set second visit
               ld C (A CDR)  # Nodes
               ld Y (C CDR)
               ld (C CDR) X
               ld X A
            loop
         loop
      loop
20    ld X (DbFiles)  # Iterate DB files
      ld Y (DBs)  # Count
      do
         ld A (X VII)  # Get 'fluse'
         null A  # Any?
         if nz  # Yes
            push A  # Save as count
            ld A X
            ld C 0  # Save Block 0 and free list
            call setBlkAC_Z  # Set up block env
            call rdBlockZ_Z  # Read first block
            do
               call logBlock  # Write to transaction log
               null (BlkLink)  # More blocks?
            while nz  # Yes
               sub (S) 1  # Decrement count
            while nb
               call rdBlockLinkZ_Z  # Read next block
            loop
            add S I  # Drop count
         end
         add X VIII  # Increment by sizeof(dbFile)
         sub Y VIII  # Done?
      until z  # Yes
      cc putc_unlocked((hex "FF") (DbLog))  # Write end marker
      cc putc_unlocked((hex "FF") (DbLog))
      cc fflush((DbLog))  # Flush Transaction log
      call logFileno_A  # Sync log file to disk
      cc fsync(A)
      nul4  # OK?
      js trSyncErrX  # No
      pop Y
      pop X
   end
   ld Y (Y CDR)  # Eval pre-expression
   ld E (Y)
   eval
   cmp (L I) Nil  # 'any'?
   if eq  # No
      push 0  # <L -I> No notification
   else
      ld A (Tell)
      or A (Children)
      push A  # <L -I> Notify flag
      if nz
         push A  # <L -II> Tell's buffer pointer
         push (TellBuf)  # <L -III> Save current 'tell' env
         sub S PIPE_BUF  # <L - III - PIPE_BUF> New 'tell' buffer
         ld Z S  # Buffer pointer
         call tellBegZ_Z  # Start 'tell' message
         ld E (L I)  # Get 'any'
         call prTellEZ  # Print to 'tell'
         ld (L -II) Z  # Save buffer pointer
      end
   end
   push X
   push Y
   ld X (Extern)  # Iterate external symbol tree
   ld Y 0  # Clear TOS
   do
      do
         ld A (X CDR)  # Get subtrees
         atom (A)  # Left subtree?
      while z  # Yes
         ld C X  # Go left
         ld X (A)  # Invert tree
         ld (A) Y  # TOS
         ld Y C
      loop
      do
         lea C ((X) TAIL)  # Get external symbol's tail
         ld A (C)
         num A  # Any properties?
         if z  # Yes
            off A SYM  # Clear 'extern' tag
            do
               lea C (A CDR)  # Skip property
               ld A (C)
               num A  # Find name
            until nz
         end
         rxl A 1  # Dirty?
         if x  # Yes
            push Y
            rxl A 1  # Deleted?
            if nx  # No
               setx  # Set "loaded"
               rxr A 1
               shr A 1
               ld (C) A  # in status/name
               ld Y A  # Name in Y
               call dbFileBlkY_AC  # Get file and block index
               cmp A (DBs)  # Local file?
               if lt  # Yes
                  call setBlockAC_Z  # Set up block env
                  call rdBlockZ_Z  # Read first block
                  ld B 1  # First block in object (might be a new object)
                  or (Z (- BLK)) B  # Set in tag byte
                  ld (PutBinBZ) putBlockBZ  # Set binary print function
                  ld Y (X)  # Get external symbol
                  ld E (Y)  # Print value
                  ld (Extn) 0  # Set external symbol offset to zero
                  call binPrintEZ
                  ld Y (Y TAIL)  # Get tail
                  off Y SYM  # Clear 'extern' tag
                  do
                     num Y  # Properties?
                  while z  # Yes
                     atom (Y)  # Flag?
                     if z  # No
                        ld E ((Y) CDR)  # Get key
                        cmp E Nil  # Volatile property?
                        if ne  # No
                           call binPrintEZ  # Print key
                           ld E ((Y))  # Print value
                           call binPrintEZ
                        end
                     else
                        ld E (Y)  # Get key
                        cmp E Nil  # Volatile property?
                        if ne  # No
                           call binPrintEZ  # Print key
                           ld E TSym  # Print 'T'
                           call binPrintEZ
                        end
                     end
                     ld Y (Y CDR)
                  loop
                  ld B NIX
                  call putBlockBZ  # Output NIX
                  ld Z (DbBlock)  # Block buffer in Z again
                  ld B (Z)  # Lowest byte of link field
                  and B BLKTAG  # Clear link
                  zxt
                  call setAdrAZ  # Store in last block
                  call wrBlockZ  # Write block
                  ld Y (BlkLink)  # More blocks?
                  null Y
                  if nz  # Yes
                     call cleanUpY  # Clean up
                  end
                  null (L -I)  # Notify?
                  if nz  # Yes
                     ld Z (L -II)  # Get buffer pointer
                     lea A ((TellBuf) (- PIPE_BUF 10))  # Space for EXTERN+<8>+END?
                     cmp Z A
                     if ge  # No
                        ld A 0  # Send to all PIDs
                        call tellEndAZ  # Close 'tell'
                        lea Z (L (- (+ III PIPE_BUF)))  # Reset buffer pointer
                        call tellBegZ_Z  # Start new 'tell' message
                        ld E (L I)  # Get 'any'
                        call prTellEZ  # Print to 'tell'
                     end
                     ld E (X)  # Get external symbol
                     call prTellEZ  # Print to 'tell'
                     ld (L -II) Z  # Save buffer pointer
                  end
               end
            else  # Deleted
               shr A 2  # Set "not loaded"
               ld (C) A  # in status/name
               ld Y A  # Name in Y
               call dbFileBlkY_AC  # Get file and block index
               cmp A (DBs)  # Local file?
               if lt  # Yes
                  add A (DbFiles)  # Get DB file
                  ld (DbFile) A  # Set current
                  ld Y C
                  call cleanUpY  # Clean up
                  null (L -I)  # Notify?
                  if nz  # Yes
                     ld Z (L -II)  # Get buffer pointer
                     lea A ((TellBuf) (- PIPE_BUF 10))  # Space for EXTERN+<8>+END?
                     cmp Z A
                     if ge  # No
                        ld A 0  # Send to all PIDs
                        call tellEndAZ  # Close 'tell'
                        lea Z (L (- (+ III PIPE_BUF)))  # Reset buffer pointer
                        call tellBegZ_Z  # Start new 'tell' message
                        ld E (L I)  # Get 'any'
                        call prTellEZ  # Print to 'tell'
                     end
                     ld E (X)  # Get external symbol
                     call prTellEZ  # Print to 'tell'
                     ld (L -II) Z  # Save buffer pointer
                  end
               end
            end
            pop Y
         end
         ld A (X CDR)  # Right subtree?
         atom (A CDR)
         if z  # Yes
            ld C X  # Go right
            ld X (A CDR)  # Invert tree
            ld (A CDR) Y  # TOS
            or C SYM  # First visit
            ld Y C
            break T
         end
         do
            ld A Y  # TOS
            null A  # Empty?
            jeq 40  # Done
            sym A  # Second visit?
            if z  # Yes
               ld C (A CDR)  # Nodes
               ld Y (C)  # TOS on up link
               ld (C) X
               ld X A
               break T
            end
            off A SYM  # Set second visit
            ld C (A CDR)  # Nodes
            ld Y (C CDR)
            ld (C CDR) X
            ld X A
         loop
      loop
   loop
40 pop Y
   pop X
   null (L -I)  # Notify?
   if nz  # Yes
      ld A 0  # Send to all PIDs
      ld Z (L -II)  # Get buffer pointer
      call tellEndAZ  # Close 'tell'
      add S PIPE_BUF  # Drop 'tell' buffer
      pop (TellBuf)
   end
   ld Y (Y CDR)  # Eval post-expression
   ld E (Y)
   eval
   null (DbJnl)  # Journal?
   if nz  # Yes
      call unLockJnl  # Unlock journal
   end
   ld Y (Zap)  # Objects to delete?
   atom Y
   if z  # Yes
      push (OutFile)  # Save output channel
      sub S (+ III BUFSIZ)  # <S> Local buffer with sizeof(outFile)
      ld E (Y CDR)  # Get zap file pathname
      call pathStringE_SZ  # Write to stack buffer
      cc open(S (| O_APPEND O_CREAT O_WRONLY) (oct "0666"))  # Open zap file
      nul4  # OK?
      js openErrEX  # No
      ld S Z  # Drop buffer
      ld (S) A  # Store 'fd' in outFile
      ld (S I) 0  # Clear 'ix'
      ld (S II) 0  # and 'tty'
      ld (OutFile) S  # Set OutFile
      ld (PutBinBZ) putStdoutB  # Set binary print function
      ld Y (Y)  # Get zap list
      do
         atom Y  # More symbols?
      while z  # Yes
         ld E (Y)  # Get next
         ld (Extn) 0  # Set external symbol offset to zero
         call binPrintEZ  # Print it
         ld Y (Y CDR)
      loop
      ld A S  # Flush file
      call flushA_F
      ld A S  # Close file
      call closeAX
      ld ((Zap)) Nil  # Clear zap list
      add S (+ III BUFSIZ)  # Drop buffer
      pop (OutFile)  # Restore output channel
   end
   null (DbLog)  # Transaction log?
   if nz  # Yes
      call fsyncDB  # Sync DB files to disk
      call truncLog  # Truncate log file
   end
   ld A 0  # Length
   call rwUnlockDbA  # Unlock all
   call unsync  # Release sync
   null (DbLog)  # Transaction log?
   if z  # No
      dec (EnvProtect)  # Unprotect
   end
   ld E (DbFiles)  # Iterate DB files
   ld C (DBs)  # Count
   do
      ld (E VII) -1  # Init 'fluse'
      add E VIII  # Increment by sizeof(dbFile)
      sub C VIII  # Done?
   until z  # Yes
   drop
   pop Z
   pop Y
   pop X
   ld E TSym  # Return T
   ret
```
