import webapp2
from hash_submit import Hash_Entry

class Hash_Retrieve(webapp2.RequestHandler):
    def get(self, id):
        q = Hash_Entry.all()
        q.filter("image_id =", id)
        
        results = q.fetch(1)
        self.response.headers['Content-Type'] = 'text/plain'
        if len(results) < 1:
            self.response.out.write("No entry found")
        else:
            self.response.out.write(str(results[0]))
        
             
                
       
   

        