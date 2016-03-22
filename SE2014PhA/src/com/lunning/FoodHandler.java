package com.lunning;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.HashSet;



import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class FoodHandler extends DefaultHandler
{
	
	private HashSet<String> hashset = new HashSet<String>();
	private String nodename = null;
	private BufferedOutputStream out = null;
	
	public HashSet<String> gethash()
	{
		return hashset;
	}
	@Override
	public void startDocument() throws SAXException 
	{
		try {
			out = new BufferedOutputStream(new FileOutputStream(new File("out.txt")));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	@Override
	public void startElement(String uri, String localName, String qName,
			Attributes attributes) throws SAXException 
	{
		nodename = qName;
	}
	
	@Override
	public void characters(char[] ch, int start, int length)
			throws SAXException 
	{
		if(nodename.equals("text"))
		{
			String str = new String(ch, start, length);
			try {
				out.write(str.getBytes());
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	
	@Override
	public void endElement(String uri, String localName, String qName)
			throws SAXException {
		// TODO Auto-generated method stub
		super.endElement(uri, localName, qName);
	}
	
	@Override
	public void endDocument() throws SAXException 
	{
		try {
			out.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
