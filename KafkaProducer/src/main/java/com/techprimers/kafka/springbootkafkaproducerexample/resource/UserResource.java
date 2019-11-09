package com.techprimers.kafka.springbootkafkaproducerexample.resource;


import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("kafka")
public class UserResource {
	private static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");
	static String numofro;
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
    
    @GetMapping("/")
    public String getnum() {
    	return numofro;
    }

    @GetMapping("/{name:.+}")
    public String post(@PathVariable("name") final String name) {

    	Timestamp timestamp = new Timestamp(System.currentTimeMillis());
        
    	int numOfRoom = Integer.parseInt(name);
    	int rate[] = {1,1,1,1,1,1,1,1,0,0};
    	
    	for(int i = 0 ; i < numOfRoom ; i ++) {
        	int rnd1 = new Random().nextInt(rate.length);
        	int rnd2 = new Random().nextInt(rate.length);
        	double temp = 25.0;
        	double max = 2.0;
        	double min = -2.0;
        	
            Random r = new Random();
            temp = temp + (min + (max - min) * r.nextDouble());
            String roomnum = "room" + (i+1);
            
            String full = roomnum + "," + rate[rnd1] + "," + rate[rnd2] + "," + sdf.format(timestamp) + "," + temp;
            //Room room = new Room(roomnum, sdf.format(timestamp) ,rate[rnd1], rate[rnd2], temp);
            
            kafkaTemplate.send(roomnum, full);
    	}
    	
    	numofro = name;

        return "this";
    }
}
