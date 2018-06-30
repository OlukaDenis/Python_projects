
import api_func
import unittest

#import apiFunc

ride_offers =[{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'30%'}]


class TestRiders(unittest.TestCase):
    # Formula for unittest method nameis..
    # test_functionName_testDescription
    # 
     def test_get_Allrides(self):
         # Test if the function get all riders 
         result = api_func.get_Allrides()
         expected = [{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'30%'}]
         # Checking for expected output
         self.assertEqual(expected,result)


class TestRider(unittest.TestCase):
#Getting a rider by id

    def test_get_ride(self):
        result = api_func.get_ride(self)
        user = [ ride for ride in ride_offers if (ride['id'] == ride_id) ] 
        expected =  user
        self.assertEqual(expected,result)
        

class TestOffer(unittest.TestCase):
    def request_ride(offer):
        ask = [ ride for ride in ride_offers if (ride['id'] == offer) ] 
        expected = ask
        self.assertEqual(expected,result)



#runing the test
 
if __name__ == '__main__':
    unittest.main() 
