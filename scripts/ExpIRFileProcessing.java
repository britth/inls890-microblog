import java.io.*;
import java.util.Iterator;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
  
class ExpIRFileProcessing {
      
    public static void main(String[] args) throws IOException {
      
          
        try {
              
            String inputLine[][][] = new String[10][][] ;
            int totalNum = 0 ;
                          
            for (int k = 1 ; k <= 10 ; k++ ) {
              
                String fileName = "output_window7_likelihood_" + Integer.toString(k) + ".txt" ;
                                  
                // Open the file that is the first 
                // command line parameter
                LineNumberReader  lnr = new LineNumberReader(new FileReader(new File(fileName)));
                lnr.skip(Long.MAX_VALUE);
                int lineNum = lnr.getLineNumber() ;
                //System.out.println(lineNum);
                  
                FileInputStream fstream = new FileInputStream(fileName);
                DataInputStream in = new DataInputStream(fstream);
                BufferedReader br = new BufferedReader(new InputStreamReader(in));
                              
                inputLine[(k-1)]= new String[lineNum + 1][];
                  
                String mLine[] = new String[lineNum + 1];
                  
                totalNum = totalNum + lineNum  ;
                //System.out.println(totalNum);
                //System.out.println(lineNum) ;
                //Read File Line By Line
                for (int i=0 ; i < lineNum ; i++)  {
                // Print the content on the console
                    inputLine[(k-1)][i] = new String[2];
                    mLine[i] = br.readLine();   
                    String[] data = mLine[i].split("\t" + " ");
                      
                    for (int j = 0 ; j < 2 ; j++ ) {
                        inputLine[(k-1)][i][j] = data[j] ;  
                        System.out.println(inputLine[(k-1)][i][j]);
                    }               
                } 
                in.close();
            }
              
              
            String orgLine[][] = new String[totalNum][2] ;
              
            for (int k = 0 ; k < (int)(totalNum/10) ; k ++ ) {
                  
                for (int i = 0 ; i < 2 ; i++ ) {
                    orgLine[(10*k)][i] = inputLine[0][k][i];
                    orgLine[(10*k)+1][i] = inputLine[1][k][i] ;
                    orgLine[(10*k)+2][i] = inputLine[2][k][i] ;
                    orgLine[(10*k)+3][i] = inputLine[3][k][i] ;
                    orgLine[(10*k)+4][i] = inputLine[4][k][i] ;
                    orgLine[(10*k)+5][i] = inputLine[5][k][i] ;
                    orgLine[(10*k)+6][i] = inputLine[6][k][i] ;
                    orgLine[(10*k)+7][i] = inputLine[7][k][i] ;
                    orgLine[(10*k)+8][i] = inputLine[8][k][i] ;
                    orgLine[(10*k)+9][i] = inputLine[9][k][i] ; 
                }   
            }
              
            LineNumberReader  lnr2 = new LineNumberReader(new FileReader(new File("queries_by_word_synsets3.txt")));
            lnr2.skip(Long.MAX_VALUE);
            int lineNum2 = lnr2.getLineNumber() ;
            //System.out.println(lineNum);
              
            FileInputStream fstream2 = new FileInputStream("queries_by_word_synsets3.txt");
            DataInputStream in2 = new DataInputStream(fstream2);
            BufferedReader br2 = new BufferedReader(new InputStreamReader(in2));
                          
            String queryLine[][] = new String[lineNum2 + 1][];
            String inputLine2[] = new String[lineNum2 + 1];
              
            for (int i=0 ; i < lineNum2 ; i++)  {
                // Print the content on the console
                inputLine2[i] = br2.readLine(); 
                String[] data = inputLine2[i].split(" ");
                queryLine[i] = new String[data.length];
                      
                for (int j = 0 ; j < data.length ; j++ ) {
                    queryLine[i][j] = data[j];
                    System.out.println(queryLine[i][j]);
                }
  
            }    
              
            String outputFileName = "queries_wordnet_window7_likelihood.xml" ;
            Util8.writeStringToFile(outputFileName, "<parameters>" + "\n");
              
            for (int i=0 ; i < lineNum2 ; i++)  {
                Util8.writeStringToFile(outputFileName, "\t" + "<query>" + "\n" + "\t\t" + "<number>" + (i+1) + "</number>" + "\n" );
                  
                StringBuilder finalStringb =new StringBuilder();
                  
                  
                for (int j=0 ; j < queryLine[i].length ; j ++) {
                      
                    int collocationNotFound = 0 ;
                      
                    outerloop: 
                    for(int k1=0 ; k1 < totalNum ; k1++ ) {
                                                  
                        for (int k2=0 ; k2 < 2 ; k2++) {
                              
                            String tempQuery = queryLine[i][j].toLowerCase() ;
                            if (tempQuery.equals(orgLine[k1][k2])) {
                                if (collocationNotFound == 0) {
                                    if (k2==0) {
                                        if (j < (queryLine[i].length)-1 || k2 == 0 ) {
                                            finalStringb.append(queryLine[i][j]).append(" ").append(orgLine[k1][1]).append(" ");
                                            //finalStringb.append("A");
                                        } else {
                                            finalStringb.append(queryLine[i][j]).append(" ").append(orgLine[k1][1]);
                                            //finalStringb.append("B");
                                        }
                                              
                                    }
                                    else {
                                        if (j < (queryLine[i].length)-1 || k2 == 0 ) {
                                            finalStringb.append(queryLine[i][j]).append(" ").append(orgLine[k1][0]).append(" ");
                                            //finalStringb.append("C");
                                        } else {
                                            finalStringb.append(queryLine[i][j]).append(" ").append(orgLine[k1][0]);
                                            //finalStringb.append("D");
                                        }
                                              
                                    }
                                }
                                else {                                  
                                    if (k2==0) {
                                        if (j < (queryLine[i].length)-1 || k2 == 0 ) {
                                            finalStringb.append(orgLine[k1][1]).append(" ");
                                            //finalStringb.append("E");
                                        } else {
                                            finalStringb.append(orgLine[k1][1]);
                                            //finalStringb.append("F");
                                        }
                                              
                                    }
                                    else {
                                        if (j < (queryLine[i].length)-1 || k2 == 0 ) {
                                            finalStringb.append(orgLine[k1][0]).append(" ");
                                            //finalStringb.append("G");
                                        } else {
                                            finalStringb.append(orgLine[k1][0]);
                                            //finalStringb.append("H");
                                        }
                                              
                                    }
                                      
                                }
                          
                                break outerloop ;
                            }
                              
                            else {
                                if (collocationNotFound == 0) {
                                    if (j < (queryLine[i].length)-1 || k2 == 0 ){
                                        finalStringb.append(queryLine[i][j]).append(" ");
                                        //finalStringb.append("I");
                                    } else {
                                        finalStringb.append(queryLine[i][j]);
                                        //finalStringb.append("K");
                                    }
                                }
                                  
                                collocationNotFound = collocationNotFound + 1 ;
                            }
                        }
                    }
                }
                  
                String finalS = finalStringb.toString();
                String[] data = finalS.split(" ");
                StringBuilder modifiedStringb =new StringBuilder();
                for (int j=0 ; j < data.length ; j++ ) {
                    if ( j == data.length - 1) {
                        modifiedStringb.append(data[j]);
                    } else {
                        modifiedStringb.append(data[j]).append(" ");
                    }   
                }
                String modifiedS = modifiedStringb.toString();
                  
                Util8.writeStringToFile(outputFileName, "\t\t" + "<text>" + modifiedS + "</text>" + "\n");
                Util7.writeStringToFile(outputFileName, "\t" + "</query>" + "\n");
            }
              
            Util8.writeStringToFile(outputFileName, "</parameters>");
            //Close the input stream
            in2.close();
              
              
        }   
          
        catch (Exception e) {//Catch exception if any
            System.err.println("Error: " + e.getMessage());         
        }
          
    }
  
}
  
class Util8 {
  
    public static void writeStringToFile(String filePathAndName, String stringToBeWritten) throws IOException{    
        try
        {
            String filename= filePathAndName;
            boolean append = true;
            FileWriter fw = new FileWriter(filename,append);
  
            fw.write(stringToBeWritten);//appends the string to the file
            //fw.write("\n");
            fw.close();
        }
  
        catch(IOException ioe)
        {
            System.err.println("IOException: " + ioe.getMessage());
        }
    }
}
