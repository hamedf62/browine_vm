from ape import accounts, project


def main():
    # Initialize deployer account and print balance
    jamshid = accounts.load("jamshid")

    print(f"The account balance is: {jamshid.balance / 1e18} Goerli ETH")

    # Deploy the smart contract and print a message
    jamshid.deploy(project.CF, 2222222)
    print("Contract deployed!")
