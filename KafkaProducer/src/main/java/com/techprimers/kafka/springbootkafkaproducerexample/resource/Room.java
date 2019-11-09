package com.techprimers.kafka.springbootkafkaproducerexample.resource;

import java.util.Date;

public class Room {
	String roomname;
	int doorstatus;
	int motionSensor;
	String date;
	double temp;

	
	
	public Room(String roomname,String date, int doorstatus, int motionSensor, double temp) {
		this.roomname = roomname;
		this.doorstatus = doorstatus;
		this.motionSensor = motionSensor;
		this.date = date;
		this.temp = temp;
	}

	
	

	public String getDate() {
		return date;
	}




	public void setDate(String date) {
		this.date = date;
	}




	public String getRoomname() {
		return roomname;
	}





	public void setRoomname(String roomname) {
		this.roomname = roomname;
	}





	public int getDoorstatus() {
		return doorstatus;
	}


	public void setDoorstatus(int doorstatus) {
		this.doorstatus = doorstatus;
	}


	public int getMotionSensor() {
		return motionSensor;
	}


	public void setMotionSensor(int motionSensor) {
		this.motionSensor = motionSensor;
	}


	public double getTemp() {
		return temp;
	}


	public void setTemp(double temp) {
		this.temp = temp;
	}
	
	

	
	

}
