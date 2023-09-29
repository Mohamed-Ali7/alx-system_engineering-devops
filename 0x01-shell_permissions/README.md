**File 0-iam_betty:** switches the current user to the user betty.  
**File 1-who_am_i:** prints the effective username of the current user.  
**File 2-groups:** prints all the groups the current user is part of.  
**Filel 3-new_owner:** changes the owner of the file hello to the user betty.  
**File 4-empty:** creates an empty file called hello.  
**File 5-execute:** adds execute permission to the owner of the file hello.  
**File 6-multiple_permissions:** execute permission to the owner and the group owner, and read permission to other users, to the file hello.  
**File 7-everybody:** xecution permission to the owner, the group owner and the other users, to the file hello.  
**File 8-James_Bond:** sets the permission to the file  `hello`  as follows:

-   Owner: no permission at all
-   Group: no permission at all
-   Other users: all the permissions
**File 9-John_Doe:** sets the mode of the file `hello` to this: 
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```
**File 10-mirror_permissions:** Write a script that sets the mode of the file  `hello`  the same as  `olleh`’s mode.

-   The file  `hello`  will be in the working directory
-   The file  `olleh`  will be in the working directory
 
