package com.lunning;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.XMLReader;

public class Main 
{
	public static void main(String[] args) throws Exception
	{
		SAXParserFactory fac = SAXParserFactory.newInstance();
		SAXParser parser = fac.newSAXParser();
		XMLReader reader = parser.getXMLReader();
		FoodHandler handler = new FoodHandler();
		reader.setContentHandler(handler);
		reader.parse("Restaurants_Train.xml");

	}

}
