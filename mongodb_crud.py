from pymongo import MongoClient, results

class Cru:
   connection = MongoClient("mongodb://localhost:27017/")

   def mongo_connection(self):
        if self.connection:
            return True
        else:
            return False
   
   def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return(new_collection)
        else:
            return("ERROR(404) : MongoDB Connection Failed !")
   
   def timestamp(self):
        import datetime as dt
        return dt.datetime.now()

    # insert data into collections
   def insert_data(self, db_name, collection_name, id, name, email, mobile):
        if self.connection:
            data = {'_id': id, 'name': name, 'email': email,
                    'mobile': mobile, 'time_stamp': self.timestamp()}
            self.connection[db_name][collection_name].insert_one(data)
            return("SUCCESS : Data Inserted !")
        else:
            return("ERROR : Unable to insert data")
    
   def display_data(self, db_name, collection_name):
        result=[]
        if self.connection:
            for data in self.connection[db_name][collection_name].find():
                result.append(data)
            for dic in result:
                for key,value in dic.items():
                    print(value)
                print()    
        else:
            return("ERROR : DB connection error !")
   def get_data(self, db_name, collection_name,ids,query):
        result=[]
        if self.connection:
            for data in self.connection[db_name][collection_name].find():
                result.append(data)
            for dic in result:
                if dic["_id"]==ids:
                  return dic[query]
        else:
            return("ERROR : DB connection error !")
    
   def update_data(self,db_name, collection_name,ids,query,crt_value,new_value):
       myquery = { query: crt_value }
       newvalues = { "$set": { query: new_value } }
       self.connection[db_name][collection_name].update_one(myquery,newvalues)
       return("update success")
   def delete_data(self,db_name, collection_name,ids):
       myquery = { "_id": ids }
       self.connection[db_name][collection_name].delete_one(myquery)
       return("delete success")    
ans=1
c=Cru()
a=c.create_new_collection('datab','crud')
#print(c.get_data('datab','crud',1,'name'))
while ans!=0:
    print ("1.Insert data")
    print ("2.View all data")
    print ("3.Update data by id")
    print ("4.Delete data by id")
    print("Press 1-4 or 0 to Exit:")
    ans=int(input())
    if ans==1:
      print()
      print("enter id,name,email,mobile") 
      _id=int(input())
      name=input()
      email=input()
      mobile=input()
      print(c.insert_data('datab', 'crud',_id, name,email,mobile))
    elif ans==2:
      c.display_data('datab','crud') 
    elif ans==3:
       q=["name","email","mobile"]
       print("enter id")
       i=int(input())
       print("1.name")
       print("2.email")
       print("3.mobile")
       opt=int(input())    
       query=q[opt-1]
       print("enter new value")
       new_value=input()
       #print(new_value)
       crt_value=c.get_data('datab','crud',i,query) 
       #print(crt_value)
       print(c.update_data('datab','crud',i,query,crt_value,new_value))

    elif ans==4:
       print("enter id")
       i=int(input())
       print(c.delete_data('datab','crud',i))

       
    elif ans==0:
      print("Goodbye") 
      ans=0
      break
    