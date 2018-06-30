from flask import Flask, jsonify, request,json

app = Flask(__name__)

# Creating a list of rider offeres
ride_offers=[{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'50%'}]


#Getting all rides
@app.route('/api/v1/rides',methods=['GET'])
def get_All_ride():
    return jsonify({'rides':ride_offers})


#Getting a rider by id
@app.route('/api/v1/rides/<ride_id>',methods=['GET'])
def get_ride(ride_id):
    user = [ ride for ride in ride_offers if (ride['id'] == ride_id) ] 
    return jsonify({'ride':user})


#ASk for offer
@app.route('/api/v1/rides/<ride_id>/requests',methods=['GET'])
def request_ride(offer):
    ask = [ ride for ride in ride_offers if (ride['id'] == offer) ] 
    return jsonify({'ride':ask})



 #create Arider 
@app.route('/api/v1/rides',methods=['POST'])
def createride():
    arider_offer = {
    'id':request.json['id'],
    'name':request.json['name'],
    'offer':request.json['offer']
    }
    ride_offers.append(arider_offer)
    return jsonify(arider_offer)

#deleting a ride (remove)
@app.route('/index/v1/rides/<ride_Id>',methods=['DELETE'])
def deleteride(ride_Id):
    remove1 = [ ride for ride in ride_offers if (ride['id'] == ride_Id) ]
    if len(remove1) == 0:
        return remove1, 200 #Success or OK
    ride_offers.remove(remove1[0])
    return jsonify({'response':'Success'})

if __name__ == '__main__':
    
    app.run()
