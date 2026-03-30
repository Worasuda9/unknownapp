# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

### Flowchart of the main workflow

```mermaid
flowchart TD
    A["Start"] --> B["initData()"]
    B --> C["LOGIN MENU"]
    C --> |1| D["Student Login"]
    C --> |2| E["Admin Login"]
    C --> |3| F["Exit + saveAndExit()"]

    D --> D1{"Student ID == \"new\"?"}
    D1 --> |Yes| D2["createStudentProfile()"]
    D1 --> |No| D3["getStudent(id)"]
    D3 --> |Null| D4["Show \"ID not found\" -> back to LOGIN MENU"]
    D3 --> |Found| D5["studentMenu(student)"]
    D2 --> |Created| D5
    D2 --> |Canceled| C

    E --> E1["Enter password"]
    E1 -->|correct| E2["adminMenu()"]
    E1 -->|wrong| E3["Show \"Incorrect password\" -> back to LOGIN MENU"]

    D5 --> C
    E2 --> C

    subgraph STUDENT_MENU
      S1["1 View Course Catalog"]
      S2["2 Register for Course"]
      S3["3 Drop Course"]
      S4["4 View Schedule"]
      S5["5 Billing Summary"]
      S6["6 Edit Profile"]
      S7["7 Logout and Save"]
      S7 --> C
      S1 --> Sx
      S2 --> Sx
      S3 --> Sx
      S4 --> Sx
      S5 --> Sx
      S6 --> Sx
      Sx["Back to studentMenu"] --> D5
    end

    subgraph ADMIN_MENU
      A1["1 View Course Catalog"]
      A2["2 View Class Roster"]
      A3["3 View All Students"]
      A4["4 Add New Student"]
      A5["5 Edit Student Profile"]
      A6["6 Add New Course"]
      A7["7 Edit Course"]
      A8["8 View Student Schedule"]
      A9["9 Billing Summary"]
      A10["10 Logout and Save"]
      A10 --> C
      A1 --> Ax
      A2 --> Ax
      A3 --> Ax
      A4 --> Ax
      A5 --> Ax
      A6 --> Ax
      A7 --> Ax
      A8 --> Ax
      A9 --> Ax
      Ax["Back to adminMenu"] --> E2
    end
```

### Prompts
Create an equivalent Python version of view course catalog feature. Put the Python program in a new folder called “python.”