const express = require('express');
const app = express();
const fs = require('fs');

app.listen(3000, () => console.log('listening at 3000'));
app.use(express.static('public'));
app.use(express.json({ limit: '1mb' }));





//app.post('/api', (request, response) => {
   // const data = request.body;
  //  const json = JSON.stringify(data);
  //  const add = json + ',';
//    console.log(add);
  //console.log(data);
//const localTime = Date.now();
//data.localtime = localTime;
//database.insert(data);

  //  fs.appendFile("iss_data1.json", add, function (err) {
  //      if (err) {
  //          console.log(err);
  //      } console.log("success");
 //   });

    //fs.writeFile("test.json", json, function (err) {
    //    if (err) {
    //        console.log(err);
   //     }
  //  });
 // response.json(data);
//});


