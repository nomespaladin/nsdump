# NsDump
# Ns Discovery Tool

nsdump is a Python script designed to help you gather information about a domain's name servers (NS records), including related IP addresses and other DNS record types. It retrieves and displays these details, providing a snapshot of the domain's DNS configuration.
## Features

-Validates domain name format using regular expressions.
- `Resolves various DNS record types (A, NS, MX, SOA, TXT, PTR) for the provided domain.`
- `Extracts IP addresses associated with name servers.`
- `Offers the option to save results to a text file with timestamps for future reference.`

## Prerequisites

- Python 3.x
- Required Python packages:
  - `os`
  - `requests`
  - `datetime` 
  - `time`
  - `dnspython`
  - `re`
  - `ipaddress`


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nomespaladin/nsdump.git
    cd nsdump
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script and enter a domain when prompted:
```sh
python nsdump.py
```
``` 
You will be prompted to save the file , 3 General locations to be prompted (case sensitive), those are : ['Desktop','Downloads','Documents']
```



## Example Overview

```sh


██████████████████████████████████████████
█▄─▀█▄─▄█─▄▄▄▄█▄─▄▄▀█▄─██─▄█▄─▀█▀─▄█▄─▄▄─█
██─█▄▀─██▄▄▄▄─██─██─██─██─███─█▄█─███─▄▄▄█
▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀
██████████████████████████████████████████

Type '-q' to exit program.

Enter Domain: example.com
Running|[15:32:47]|[02/12/2024]|

--- DNS Relations for example.com --- 
Related Name Server : ns1.example.com | Type: NS | IP : 192.168.1.1
Related Name Server : ns2.example.com | Type: NS | IP : 10.0.0.1

Would you like to save the file?('yes'/'no'/'-q'[to quit]): yes

Select option,type: 'Desktop' | 'Documents' | 'Downloads' |
Enter Directory to save the file: Documents
File is was saved >> /home/your_username/Documents/ns_results_example.com.txt



```
