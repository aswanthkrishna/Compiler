# Compiler 

A compiler for adding decimal representations on quantum computer

### Prerequisites

- python ^3.9
- poetry [package manager]
- qiskit

can also be run in Docker using the included dockerfile

### Instructions

1. build the docker image `docker build . -t compiler`


### Sample Output

`docker run compiler`

```           encode x0       encode x1                                                                     add 
q_0: ──────────░───────────────░──────────■───────────────────────────────────────────────────────────────░──
     ┌───┐     ░               ░          │                                                               ░  
q_1: ┤ X ├─────░───────────────░──────────┼──────────■────────────────────────────────────────────────────░──
     └───┘     ░               ░          │          │                                                    ░  
q_2: ──────────░───────────────░──────────┼──────────┼──────────■─────────────────────────────────────────░──
               ░               ░          │          │          │                                         ░  
q_3: ──────────░───────────────░──────────┼──────────┼──────────┼──────────■──────────────────────────────░──
               ░               ░          │          │          │          │                              ░  
q_4: ──────────░───────────────░──────────┼──────────┼──────────┼──────────┼──────────■───────────────────░──
               ░     ┌───┐     ░          │          │          │          │          │                   ░  
q_5: ──────────░─────┤ X ├─────░──────────┼──────────┼──────────┼──────────┼──────────┼──────────■────────░──
               ░     └───┘     ░          │          │          │          │          │          │        ░  
q_6: ──────────░───────────────░──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼────────░──
               ░               ░     ┌────┴────┐┌────┴────┐┌────┴────┐┌────┴────┐┌────┴────┐┌────┴─────┐  ░  
q_7: ──────────░───────────────░─────┤ Rx(π/2) ├┤ Rx(π/4) ├┤ Rx(π/8) ├┤ Rx(π/4) ├┤ Rx(π/8) ├┤ Rx(π/16) ├──░──
               ░               ░     └─────────┘└─────────┘└─────────┘└─────────┘└─────────┘└──────────┘  ░  ```