import tornado.web

Dictionary={
    "alice":{
            "name" : "Alice Smith",
            "dob" : "Jan. 1",
            "email" : "alice@example.com"
        },
    "bob":{
            "name" : "Bob Jones",
            "dob" : "Dec. 31",
            "email" : "bob@bob.xyz"
        },
    "carol":{
            "name" : "Carol Ling",
            "dob" : "Jul. 27",
            "email" : "carol@example.com"
        },
    "dave":{
            "name" : "Dave N. Port",
            "dob" : "Mar. 14",
            "email" : "dave@dave.dave"
        },
}
    
class Handler(tornado.web.RequestHandler):
    def get(self):
        #q = random.choice(quotes)
        #self.render( "TemplateTest.html", quotation=q )

        L = self.request.path.split("/")
        uname = L[2]
        info = Dictionary[uname]
        
        self.render("profilepage.html",
        name=info["name"], dateofbirth=info["dob"],
        email=info["email"])


    #D={
    #"alice":{
            #"name" : "Alice Smith",
            #"dob" : "Jan. 1",
            #"email" : "alice@example.com"
        #},
    #"bob" ...
    #}

    #get()
        #L = self.request.path.split("/")
        #uname = L[2]
        #info = D[uname]
        #self.render("profilepahe.html",
        #    name=info["name"], dateofbirth=info["dob"],
        #    email=info["email"])

    # or...
        #info[0] //Name
        #info[1] //DOB
        #info[2] //Email