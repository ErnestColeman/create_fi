"""
Create FI 
"""

def createFI():
    with open("sh.txt", mode="w") as dataFile:
        dataFile.write("==================================\n" \
            "*Symptoms and Customer Environment*\n" \
            "==================================\n" \
            "*Reason for FI*:\n\n" \
            f"{reason}\n" \
            "*FI reviewed by*:\n\n" \
            f"{approver}\n" \
            "*Upgrade history and current version*:\n\n" \
            f"{upgrade_history} | {private_binaries}"
            
                )

reason =  input("What is the reason for the FI/SH?: ")
approver = input("Who was the Tech Lead or Senior SRE that has approved this?: ")

poc = input("Is this a POC case (yes or no)? ").lower()


if poc == "yes":
    print("The following questions are Optional\n")
    topology = input("What is the environment topology?\n" \
        "e.g. VMware Backup, SQL, Oracle, Netapp, Veeam Dumps, Hyper-V backup, Replication, Cloud Archival, S3 , Fileservices, *Protection job and policy information*: ")

private_binaries = input("Are private binaries installed? (hc_cli run -v --test-ids=10003) *Version ONLY* ")



if __name__ == "__main__":
    createFI()
