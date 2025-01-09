graph TD
    A[Start] --> B[Choose weight class]
    B -->|lightweight/middleweight| C[Set fighters to lightweight_middleweight_fighters]
    B -->|heavyweight| D[Set fighters to heavyweight_fighters]
    B -->|Invalid| E[Print "Invalid weight class selection"]
    E --> B

    C --> F[Choose mode]
    D --> F

    F -->|single| G[Ask for user control]
    F -->|tournament| H[Print available fighters]
    F -->|Invalid| I[Print "Invalid mode selection"]
    I --> F

    G -->|yes| J[Print available fighters]
    G -->|no| K[Randomly select user and opponent fighters]

    J --> L[Choose user fighter]
    L --> M[Choose opponent fighter]
    M --> N[Get user fighter]
    N --> O[Get opponent fighter]

    K --> P[Get user fighter]
    K --> Q[Get opponent fighter]

    O --> R[Check if fighters are valid]
    P --> R
    Q --> R

    R -->|valid| S[Call fight function]
    R -->|Invalid| T[Print "Invalid fighter selection"]

    S -->|win| U[Increment wins]
    S -->|loss| V[Increment losses]

    H --> W[Choose user fighter]
    W --> X[Get user fighter]
    X --> Y[Check if fighter is valid]
    Y -->|valid| Z[Call tournament function]
    Y -->|Invalid| AA[Print "Invalid fighter selection"]

    Z -->|win| U
    Z -->|loss| V