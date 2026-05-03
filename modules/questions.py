import random

QUESTIONS = {

    # ===================== DSA =====================
    "dsa": {

        "easy": [
            {
                "question": "What is a linked list?",
                "keywords": ["node", "pointer", "data"],
                "answer": "A linked list is a linear data structure where each element is a node containing data and a pointer to the next node."
            },
            {
                "question": "What is a stack?",
                "keywords": ["lifo", "push", "pop"],
                "answer": "A stack is a linear data structure that follows the Last In First Out principle where elements are added using push and removed using pop."
            },
            {
                "question": "What is a queue?",
                "keywords": ["fifo", "enqueue", "dequeue"],
                "answer": "A queue is a linear data structure that follows First In First Out order where elements are inserted using enqueue and removed using dequeue."
            }
        ],

        "medium": [
            {
                "question": "What is a binary search tree?",
                "keywords": ["tree", "left", "right", "sorted"],
                "answer": "A binary search tree is a binary tree where each node's left child contains smaller values and the right child contains larger values."
            },
            {
                "question": "Explain quick sort algorithm.",
                "keywords": ["pivot", "partition", "divide"],
                "answer": "Quick sort is a divide and conquer algorithm that selects a pivot element and partitions the array recursively."
            },
            {
                "question": "What is hashing?",
                "keywords": ["hash", "key", "index"],
                "answer": "Hashing converts a key into an index using a hash function to enable fast data retrieval."
            }
        ],

        "hard": [
            {
                "question": "Explain AVL tree rotations.",
                "keywords": ["balance", "rotation", "height"],
                "answer": "AVL tree rotations maintain balance in a self balancing binary search tree when height difference exceeds one."
            },
            {
                "question": "Explain dynamic programming.",
                "keywords": ["optimal", "subproblem", "memoization"],
                "answer": "Dynamic programming solves problems by breaking them into overlapping subproblems and storing intermediate results."
            },
            {
                "question": "What is a segment tree?",
                "keywords": ["range", "query", "tree"],
                "answer": "A segment tree is a binary tree used for efficient range queries and updates on arrays."
            }
        ]
    },

    # ===================== DBMS =====================
    "dbms": {

        "easy": [
            {
                "question": "What is a primary key?",
                "keywords": ["unique", "identifier", "table"],
                "answer": "A primary key uniquely identifies each record in a database table."
            },
            {
                "question": "What is a foreign key?",
                "keywords": ["reference", "relationship", "table"],
                "answer": "A foreign key is a field that references the primary key of another table to establish relationships."
            },
            {
                "question": "What is SQL?",
                "keywords": ["query", "database", "language"],
                "answer": "SQL is a structured query language used to manage and manipulate relational databases."
            }
        ],

        "medium": [
            {
                "question": "What is normalization?",
                "keywords": ["redundancy", "normal", "form"],
                "answer": "Normalization organizes data to reduce redundancy and improve data integrity."
            },
            {
                "question": "Explain indexing.",
                "keywords": ["index", "search", "performance"],
                "answer": "Indexing improves database performance by enabling faster data retrieval."
            },
            {
                "question": "What are joins?",
                "keywords": ["combine", "tables", "rows"],
                "answer": "Joins combine rows from multiple tables based on related columns."
            }
        ],

        "hard": [
            {
                "question": "Explain ACID properties.",
                "keywords": ["atomicity", "consistency", "isolation", "durability"],
                "answer": "ACID properties ensure reliable database transactions through atomicity, consistency, isolation and durability."
            },
            {
                "question": "What is transaction management?",
                "keywords": ["transaction", "commit", "rollback"],
                "answer": "Transaction management ensures database operations are executed reliably and can be committed or rolled back."
            },
            {
                "question": "Explain concurrency control.",
                "keywords": ["lock", "transaction", "conflict"],
                "answer": "Concurrency control manages simultaneous transactions to prevent conflicts and maintain consistency."
            }
        ]
    },

    # ===================== NETWORKS =====================
    "networks": {

        "easy": [
            {
                "question": "What is an IP address?",
                "keywords": ["address", "network", "device"],
                "answer": "An IP address uniquely identifies a device on a network."
            },
            {
                "question": "What is DNS?",
                "keywords": ["domain", "name", "ip"],
                "answer": "DNS translates domain names into IP addresses."
            },
            {
                "question": "What is HTTP?",
                "keywords": ["protocol", "web", "request"],
                "answer": "HTTP is a protocol used for transferring web pages between clients and servers."
            }
        ],

        "medium": [
            {
                "question": "Explain TCP vs UDP.",
                "keywords": ["connection", "reliable", "protocol"],
                "answer": "TCP is a reliable connection oriented protocol while UDP is connectionless and faster but unreliable."
            },
            {
                "question": "What is subnetting?",
                "keywords": ["network", "division", "ip"],
                "answer": "Subnetting divides a network into smaller subnetworks for better management."
            },
            {
                "question": "What is a router?",
                "keywords": ["network", "packet", "forward"],
                "answer": "A router forwards data packets between different networks."
            }
        ],

        "hard": [
            {
                "question": "Explain OSI model layers.",
                "keywords": ["layer", "application", "transport"],
                "answer": "The OSI model consists of seven layers describing how data moves across a network."
            },
            {
                "question": "What is congestion control?",
                "keywords": ["network", "traffic", "control"],
                "answer": "Congestion control regulates data transmission to prevent network overload."
            },
            {
                "question": "Explain NAT.",
                "keywords": ["address", "translation", "private"],
                "answer": "Network Address Translation allows multiple private IP addresses to share a single public IP."
            }
        ]
    },

    # ===================== OS =====================
"os": {

    "easy": [
        {
            "question": "What is an operating system?",
            "keywords": ["interface", "hardware", "software"],
            "answer": "An operating system is system software that acts as an interface between the user and hardware and manages system resources."
        },
        {
            "question": "What is a process?",
            "keywords": ["execution", "program", "running"],
            "answer": "A process is a program in execution that includes its code, data, and resources."
        },
        {
            "question": "What is a thread?",
            "keywords": ["lightweight", "process", "execution"],
            "answer": "A thread is the smallest unit of execution within a process."
        }
    ],

    "medium": [
        {
            "question": "What is scheduling in OS?",
            "keywords": ["cpu", "process", "scheduler"],
            "answer": "Scheduling is the process of selecting which process gets CPU time using scheduling algorithms."
        },
        {
            "question": "Explain deadlock.",
            "keywords": ["waiting", "resource", "cycle"],
            "answer": "Deadlock is a situation where processes are stuck waiting for each other’s resources indefinitely."
        },
        {
            "question": "What is virtual memory?",
            "keywords": ["memory", "paging", "disk"],
            "answer": "Virtual memory allows execution of processes without requiring all data to be in physical memory."
        }
    ],

    "hard": [
        {
            "question": "Explain paging.",
            "keywords": ["page", "frame", "memory"],
            "answer": "Paging divides memory into fixed-size pages and frames to manage memory efficiently."
        },
        {
            "question": "What is thrashing?",
            "keywords": ["paging", "performance", "swap"],
            "answer": "Thrashing occurs when excessive paging leads to low CPU utilization and high disk activity."
        },
        {
            "question": "Explain synchronization.",
            "keywords": ["critical", "section", "mutex"],
            "answer": "Synchronization ensures that multiple processes do not access shared resources simultaneously causing inconsistency."
        }
    ]
},

# ===================== HR =====================
"hr": {
    "easy": [
        {
            "question": "Tell me about yourself",
            "keywords": ["background", "skills", "experience"],
            "answer": "I am a motivated individual with a strong background in my field, skilled in problem solving and eager to learn and grow."
        },
        {
            "question": "Why should we hire you?",
            "keywords": ["skills", "value", "contribution"],
            "answer": "You should hire me because I bring strong skills, dedication, and the ability to contribute effectively to your team."
        },
        {
            "question": "What are your strengths and weaknesses?",
            "keywords": ["strength", "weakness", "improvement"],
            "answer": "My strength is problem solving and adaptability, and my weakness is overthinking which I am actively improving."
        }
    ]
},


# ===================== BEHAVIORAL =====================
"behavioral": {
    "easy": [
        {
            "question": "Tell me about a challenge you faced",
            "keywords": ["challenge", "solution", "result"],
            "answer": "I faced a challenge where I had to solve a difficult problem, and I overcame it by breaking it into smaller parts and finding a solution."
        },
        {
            "question": "Describe a time you worked in a team",
            "keywords": ["team", "collaboration", "communication"],
            "answer": "I worked in a team where we collaborated effectively, communicated clearly, and successfully completed the task."
        },
        {
            "question": "How do you handle pressure?",
            "keywords": ["pressure", "calm", "focus"],
            "answer": "I handle pressure by staying calm, prioritizing tasks, and focusing on solutions instead of problems."
        }
    ]
}
}

# ======================================================
# Function to Fetch Random Questions
# ======================================================

def get_questions(subject, difficulty, count=3):
    subject = subject.lower()

    subject_data = QUESTIONS.get(subject, QUESTIONS["dsa"])
    level_questions = subject_data.get(difficulty, subject_data["easy"])

    questions = level_questions.copy()
    random.shuffle(questions)

    return questions[:count]