# keysafe
 Keyring-based utilitiy for enhanced safekeeping of login information. 

Many websites require user's email address as a user login id. You may want to avoid accidentally revealing these addresses, especially if your scripts are hosted publicly. **keysafe** provides a way to hide not only the passwords but also the user id's by using aliases instead. The actual login info is saved in the keychain and retrieved using the standard **keyring** library.

In other words, keys themselves are hidden in a safe.  

### Examples of use: ###

#### *Create a record* ####

\>>>from keysafe import safe

\>>>x=safe()

\>>>x.service='MYSAFE'

\>>>x.alias='John'

\>>>x.user=`'john@mail.com'`

\>>>x.password='$WhoopsyDaisies01'

\>>>x.set()


#### *Retreive user id and passwrod* ####

\>>> y=safe()

\>>> y.service='MYSAFE'

\>>> y.alias='John'

\>>> y.get()

\>>> y.user

`'john@mail.com'`

\>>> y.password

'$WhoopsyDaisies01' 




