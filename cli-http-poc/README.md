## Directory structure
    .
    ├── data
    │   ├── CC
    │   │   ├── validateBRN
    │   │   │   ├── v1                          # Version 1
    │   │   │   │   ├── UC01                    # Use case 01
    │   │   │   │   │   ├── Body.json
    │   │   │   │   │   ├── Auth.json
    │   │   │   │   │   ├── Query.json
    │   │   │   │   │   ├── Header.json
    │   │   │   │   │   └── Docs.json
    │   │   │   │   ├── UC02                    # Use case 02
    │   │   │   │   └── UC03                    # Use case 03
    │   │   │   └── v2
    │   │   │       ├── UC01
    │   │   │       └── UC02
    │   │   ├── getCustomerDetaills
    │   │   └── README.md                       # Only system related information (CC)
    │   └── SL
    │       ├── getContractDetails
    │       │   └── v1                          # Version
    │       │       └── UC01                    # Use case 01
    │       └── README.md                       # Only system related information (SL)
    ├── docs                                    # Documentation files (Shall be all in markdown)
    │   └── README.md                           # Holds information about systems
    ├── tests                                   # Test Cases
    └── requirements.txt                        # Dependencies

---
## Arguments

| Argument  |   Description |   Example |
| :---        |    :----   |          :---: |
| system      | Same as the Directory name | CC   |
| interface   | Interface Name | getCustomerDetails     |
| version   |   Version     | v1 |
| useCase   |   Use Case     | UC01 |   
|httpMethod |   HTTP Method   | GET |
|ws     |   Web Service type   |REST    |

---

- SOAP
  - https://docs.python-zeep.org/en/master/
- REST


### cli -system=SL -interface=getCustomer -version=v1 useCase=uc01 