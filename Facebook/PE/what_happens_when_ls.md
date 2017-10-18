# What happens when you enter `ls -al`

This is an attempt to answer the famous Facebook Production Engineering question, "What happens when you enter `ls -al`"

1. Your shell program tries to find what `ls -al` means, specificall
    * Check if `ls` is an alias, if it is, resolve the whole command
    * Check if `ls` is a shell built-in 
    * Find `ls` in the `PATH` enviornment 
2. If `ls` is found, shell will call the following system calls
    1. `fork()` itself, create a child process, specifically
        * Call `clone()` with specific flags to indicate shared resources between parent and child process
        * `clone()` calls `do_fork()`, which calls `copy_process()`, which does the following
            - Creates a new kernel stack, a `thread_info` struct, a `task_struct` for the new process (values are copied from the parent process)
            - Checks the new child will not exceed the resources limit on the current user
            - Change some of the process descriptor to inital/default values
            - Change child to `TASK_UNINTERRUPTED`
            - Copy flags
            - Assign PID
            - Copy necessary resources (open files, address space, signal handlers)
        * Kernel will schedule the child to run first, avoid copy-on-write overhead if otherwise

    2. `exec('ls', '-al')` execute the `ls -al` with the found executable `ls` program, specifically
        * the child calls the C library method `exec()`, change the `eax` register to appropriate system call number
        * a software interrupt was incurred, kernel captures it, context switch
        * the system call handler `system_call()` calls the actual system call `exec()`
    3. shell `wait()` for the child process to complete
    4. `ls` gets executed, it does the following
        * 
    5. child process `exit()`