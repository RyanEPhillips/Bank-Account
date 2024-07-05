# BankAccount Class for Managing Bank Accounts

The `BankAccount` class provides functionality to manage individual bank accounts, including depositing funds, withdrawing funds, checking balances, and displaying account information. Each bank account is uniquely identified by an account number and associated with an account holder.

## Class Structure

### Attributes
- **Private Attributes:**
  - `__accountNumber`: Unique identifier for each bank account.
  - `__balance`: Current balance of the bank account.
  
- **Protected Attribute:**
  - `_accountHolder`: Name of the account holder.

### Methods

#### Constructor (`__init__`)
- Initializes a new bank account with the given `accountNumber`, `accountHolder`, and `balance`.

#### Class Method (`createNewAccount`)
- Generates a random `accountNumber` and creates a new `BankAccount` instance with initial deposit specified by `initialDeposit`.

#### Property (`accountNumber`)
- Provides read-only access to the private attribute `__accountNumber`.

#### Deposit Method (`deposit`)
- Increases the balance of the bank account by the specified `amount`.
- Provides feedback on successful deposit including the account holder's name and updated balance.

#### Withdrawal Method (`withdrawal`)
- Decreases the balance of the bank account by the specified `amount`, if sufficient funds are available.
- Provides feedback on successful withdrawal including the account holder's name and updated balance.
- Displays an error message if there are insufficient funds.

#### Get Balance Method (`getBalance`)
- Retrieves and prints the current balance of the bank account.
- Displays a message indicating whether the account holder has funds available or no money.

#### Display Account Info Method (`displayAccountInfo`)
- Prints detailed information about the bank account, including the account holder's name, account number, and current balance.

## Usage Example

The example demonstrates creating multiple bank accounts, performing transactions such as deposits and withdrawals, and displaying updated account information after each transaction.

```python
import random

class BankAccount:
    def __init__(self, accountNumber, accountHolder, balance):
        self.__accountNumber = accountNumber
        self._accountHolder = accountHolder
        self.__balance = balance

    @property
    def accountNumber(self):
        return self.__accountNumber

    @classmethod
    def createNewAccount(cls, accountHolder, initialDeposit):
        a
