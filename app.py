from question import question
question_prompts = [
         "what are the primary purpose of an ORM tool in back end development\n(a)Enhancing frontenduser experience\n(b)facilitating communication between microservices\n(c)simplifying database in interaction ny mapping objects to data base tables\n(d)optimizing sever-side caching mechanisms\n\n" ,
         "In the context of RESTful APIs,what does the acronym HATEOAS stands for?\nHypermedia asynchronous transfer of entities over SSL\n(b)Hypermedia As the engine of application state\n(c)high availability transmission for efficient online application systems\n(d)Hierarchical access token for enhanced object serialization\n\n" ,
         "What is the purpose of JWT in authentication within a back-end system\n(a)Encoding complex JSON structures for efficient data transmission\n(b)Ensuring secure communication  between frontenf and backend\n(c)Providing a compact,self-contained way to transmit information between parties\n(d)Enforcing strict type checking for API requests\n\n" ,
         "Which data base consistency level in distributed systems ensures that all replicas are upadated before considering a write opeation successful ?\n(a)Eventual consistency\n(b)Strong consistency\n(c)Casual consistency\n(d)Read-Your-Write consistency\n\n" ,
         "What is the purpose of the OPTIONS HTTP method in the context of a RESTful API?\n(a)Retrieving resource representations\n(b)Checking the validity of a resource\n(c)Handling pre-flight requests to support cross-origin resource sharing\n(d)Updating resource data\n\n"

]

questions = [
     question(question_prompts[0], "c"),
     question(question_prompts[1], "b"),
     question(question_prompts[2], "c"),
     question(question_prompts[3], "b"),
     question(question_prompts[4], "c"),
  ]
    
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1

    print("you got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)



