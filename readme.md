## Peer to Peer Payment App

### Problem Statement
For this problem we want to write a small piece of the backend for a peer to peer payment app. The functionality that we want for this problem are: adding users to the app, users depositing money into the app, users sending money to other app users, users checking their balance in the app, and users transferring their money out of the app. We will also write unit tests for the solution to ensure that all functionality as described above are working properly.
 
### Testing Procedure
Example Run through of the app:
User A is added to the app
User A deposits 10 dollars
User B is added to the app
User B deposits 20 dollars
User B sends 15 dollars to User A
User A checks their balance and has 25 dollars
User B checks their balance and has 5 dollars
User A transfers 25 dollars from their account
User A checks their balance and has 0 dollars

NB: Ensure pytest is install before running tests