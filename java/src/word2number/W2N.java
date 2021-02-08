/**
 * SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
 * SPDX-License-Identifier: MIT
 */
package word2number;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Locale;

/**
 * 
 * Word2Number implementation
 * 
 * This class implements an easy algorithm to translate number words to numbers from sentences.
 * It takes a <code>CharSequence</code> like <code>String</code>, <code>StringBuilder</code> or 
 * <code>StringBuffer</code> instances and returns as result <code>null</code> or an 
 * <code>Number</code> instance.
 * On other Objects the <code>toString</code> method is using to create a CharSequence on-the-fly.
 * 
 * @author Sͬeͥbͭaͭsͤtͬian
 *
 */
public class W2N {
  
  private final HashMap<String, Object> filebasedNumberSystem;
  private final HashMap<String, String> normalizeData;
  private final ArrayList<String> decimalWords;
  private final ArrayList<Long> sortedMeasureValues;
  
  private final String lang;
  
  public W2N () {
    try {
      String newLang = null;
      if (System.getenv("w2n.lang") != null)
        newLang = System.getenv("w2n.lang");
      if (newLang == null)
          newLang = Locale.getDefault().getLanguage();
      if (newLang == null)
        if (System.getenv("LANGUAGE") != null)
          newLang = System.getenv("LANGUAGE");
      if (newLang == null)
          newLang = "en";  // fallback
      this.lang = newLang.substring(0,2);
  
      this.filebasedNumberSystem = new HashMap<>();
      this.decimalWords = new ArrayList<>(10);
      this.normalizeData = new HashMap<>();
      this.sortedMeasureValues = new ArrayList<>();
      final InputStream dataFile = this.getClass().getResourceAsStream("data/config_"+this.lang+".properties");
      final BufferedReader numberSystemData = new BufferedReader( new InputStreamReader(new BufferedInputStream(dataFile,40960),"utf-8"));
      String line = null;
      int zeroToNine = 0;
      while ((line = numberSystemData.readLine()) != null) {
        if (line.startsWith("#")) {
        }
        else {
          String[] keyValue = line.split("=",2);
          String key = keyValue[0];
          Object val = keyValue[1];
          if (key.startsWith("replace:")) {
            key = key.substring("replace:".length());
            normalizeData.put(key,val.toString().trim());
          }
          else if (key.startsWith("measure:")) {
            sortedMeasureValues.add(Long.valueOf(val.toString().trim()));
          }
          else if (!"point".equals(key)) {
            val = Long.valueOf(val.toString());
          }
          this.filebasedNumberSystem.put(key, val);
          if (zeroToNine<10) {
            this.decimalWords.add(key);
            zeroToNine++;
          }
        }
      }
      Collections.sort(sortedMeasureValues,Collections.reverseOrder());
    }
    catch (Throwable t) {
      throw new RuntimeException(t);
    }
  }
  

  /**
   * function to form numeric multipliers for million, billion, thousand etc.
   * @param numberWords list of strings
   * @return value: integer
   */
  protected int numberFormation (List<String> numberWords) {
    int[] numbers = new int [numberWords.size()];
    for (int i = 0; i < numberWords.size(); i++) {
      numbers[i] = Integer.valueOf(filebasedNumberSystem.get(numberWords.get(i)).toString());
    }
    if (lang.equals("ru")){
      if (numbers.length > 3) {
        if (numbers[0] < 100) {
          numbers[0] = numbers[0] * 100;
        }
      }

      if (numbers.length == 4)
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3];
      else if (numbers.length == 3) // TODO: why are else here?
        return numbers[0]+numbers[1]+numbers[2];
      else if (numbers.length == 2) // TODO: why are else here?
        return numbers[0]+numbers[1];
      else // TODO: why are else here?
        return numbers[0];
    }
    else{
      if (numbers.length == 4)
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3];
      else if (numbers.length == 3) // TODO: why are else here?
        return numbers[0] * numbers[1] + numbers[2];
      else if (numbers.length == 2)
        if (100 == numbers [0] || 100 == numbers [1])
          return numbers[0] * numbers[1];
        else
          return numbers[0] + numbers[1];
      else
        return numbers[0];
    }
  }


  /**
   * function to convert post decimal digit words to numerial digits
   * it returns a string to prevert from floating point conversation problem
   * @param decimalDigitWords list of strings
   * @return string
   */
  protected String getDecimalString(List<String> decimalDigitWords) {
    String decimalNumberStr = ""; // TODO: check python in result of do not need an array in Java
    for (String decWord : decimalDigitWords) {
      if(!decimalWords.contains(decWord))
        return "0";
      else
        decimalNumberStr += filebasedNumberSystem.get(decWord);
    }
    final String finalDecimalString = decimalNumberStr; // TODO remove line
    return finalDecimalString;
  }
  
  /**
   * function to return integer for an input `newNumberValue` string
   * @param newNumberValue numberValue
   * @return Number or null
   */
  public Number wordToNum (Number newNumberValue) {
    if (null == newNumberValue) // same as python
      throw new NumberFormatException("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");

    return newNumberValue;
  }
  
  /**
   * Method to return integer for an input `newObjectToStringIsNumeric` string
   * @param newObjectToStringIsNumeric
   * @return Number or null
   */
  protected Number wordToNum (Object newObjectToStringIsNumeric) {
    if (null == newObjectToStringIsNumeric)
      throw new NumberFormatException("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");
    else 
      return this.wordToNum(newObjectToStringIsNumeric.toString());
  }
  /**
   * Method to return integer for an input `newNumberSentence` string
   * @param numberSentence text
   * @return Number, prefered Long and Double, or null
   */
  public Number wordToNum (CharSequence newNumberSentence) {
    Number result = null;
    LinkedList<String> cleanNumbers = new LinkedList<>();
    LinkedList<String> cleanDecimalNumbers = new LinkedList<>();

    if (null == newNumberSentence)
      throw new NumberFormatException("Type of input is null! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");

    String numberSentence = this.normalize(newNumberSentence.toString());

    // return the number if user enters a number string
    try { 
      result = Long.valueOf(newNumberSentence.toString()); 
    }
    catch (NumberFormatException noIntMaybeFloat) {
      try {
        result = Double.valueOf(newNumberSentence.toString());
      }
      catch (NumberFormatException okMoreSpecificAlgorithmNeeded) {}
    }

    final boolean isDigit = result != null; // maybe to optimize by compiler but to similar code to python 
    if (!isDigit) {
      String [] splitWords = numberSentence.split("[\\s,]+"); // strip extra spaces and comma and than split sentence into words
      String localizedPointName = this.filebasedNumberSystem.get("point").toString();
      
      // removing and, & etc.
      for (String word : splitWords) {
        if (this.filebasedNumberSystem.containsKey(word)) {
          cleanNumbers.add(word);
        }
        else if (word.equals(localizedPointName)){
          cleanNumbers.add(word);
        }
      }
  
      // Error message if the user enters invalid input!
      if (cleanNumbers.size()== 0) 
          throw new NumberFormatException("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");

      final boolean toMuchPoints = cleanNumbers.indexOf(localizedPointName) != cleanNumbers.lastIndexOf(localizedPointName);
      if (toMuchPoints)
        throw new NumberFormatException(String.format("Redundant point word %s! Please enter a valid number word (eg. two million twenty three thousand and forty nine)",localizedPointName));
  
      // separate decimal part of number (if exists)
      boolean pointCount = cleanNumbers.indexOf(localizedPointName)>-1;
      if (pointCount) {
        cleanDecimalNumbers = new LinkedList<>(cleanNumbers.subList(cleanNumbers.indexOf(localizedPointName)+1, cleanNumbers.size()));
        cleanNumbers = new LinkedList<>(cleanNumbers.subList(0,cleanNumbers.indexOf(localizedPointName)));
      }
      // special case "point" without pre or post number   
      if (cleanDecimalNumbers.size() == 0 && cleanNumbers.size() == 0) return Integer.valueOf(0);

      // check measure word errors
      List<Integer>measureWordsSequence = new LinkedList<>();
      // check for to much measure words like "million million"
      for (Long measureValueDoubleCheck : sortedMeasureValues) {
        if (measureValueDoubleCheck >= 1000) { // measure values under 1000 can be more than one in text
          checkDoubleInput(measureValueDoubleCheck, cleanNumbers);
          // save index for next check
          if (-1 != getIndexForNumber(measureValueDoubleCheck,cleanNumbers)){
            measureWordsSequence.add(getIndexForNumber(measureValueDoubleCheck,cleanNumbers));
          }
        }
      }
      
      List<Integer> sortedMeasureWordsSequence = new LinkedList<>(measureWordsSequence);
      Collections.sort(sortedMeasureWordsSequence);
      for (int i = 0; i <measureWordsSequence.size();i++) {
        if (!measureWordsSequence.get(i).equals(sortedMeasureWordsSequence.get(i))) {
          throw new NumberFormatException ("Malformed number in result of false measure word sequence eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
        }
      }
      
      // normalize measure words with add localized value for 1 before than empty
      boolean lastWasMeasureWord = true;
      LinkedList<String> normalizedCleanNumbers = new LinkedList<>(); 
      LinkedList<String> measureNames = new LinkedList<>();
      for (Long value : sortedMeasureValues) {
        measureNames.add(getNameByNumberValue(value));
      }
      for (String nextPart : cleanNumbers) {
        if (measureNames.contains(nextPart) && lastWasMeasureWord) {
          normalizedCleanNumbers.add(this.getNameByNumberValue(1L));
          lastWasMeasureWord = true;
        }
        else {
          lastWasMeasureWord = measureNames.contains(nextPart); 
        }
        normalizedCleanNumbers.add(nextPart);
      }
      cleanNumbers = normalizedCleanNumbers;


      // check no measure words in decimal numbers
      for (Long measureValue : sortedMeasureValues) {
          String measure_name = getNameByNumberValue(measureValue);
          if (cleanDecimalNumbers.contains(measure_name))
            throw new NumberFormatException ("Malformed number in result of false measure word after point eg. trillion after thousand! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
      }
      
      // Now we calculate the pre-decimal value
      result = getNumberValue(cleanNumbers);
      
      // And add the post-decimal value
      if (cleanDecimalNumbers.size() > 0){
        String decimalValue = getDecimalString(cleanDecimalNumbers);
        decimalValue = ""+result+"."+decimalValue;
        if (decimalValue.substring(decimalValue.indexOf(".")).equals(".0")) {
          decimalValue = decimalValue.substring(0, decimalValue.indexOf("."));
          Long value = Long.valueOf(decimalValue);
          result = value;
          if (value.longValue() < Long.valueOf(Integer.MAX_VALUE).longValue() &&
              value.longValue() > Long.valueOf(Integer.MIN_VALUE).longValue()) {
            result = Integer.valueOf(value.intValue());
          }
        }
        else {
          result = Double.valueOf(decimalValue);
        }
      }
    }
    if (result instanceof Long) {
      if (result.longValue() < Long.valueOf(Integer.MAX_VALUE).longValue() &&
          result.longValue() > Long.valueOf(Integer.MIN_VALUE).longValue()) {
        result = Integer.valueOf(result.intValue());
      }
    }
    return result;
  
  }
  

  /**
   * Method to normalize the whole(!) input text
   * @param numberSentence input string
   * @return normalized input
   */
  protected String normalize(String numberSentence) {
    numberSentence = numberSentence.toLowerCase(new Locale(this.lang));  // converting input to lowercase
    numberSentence = numberSentence.replace ("-"," ");

    // for examples: both is right "vingt et un" and "vingt-et-un"
    // we change this to composed value "vingt-et-un" over the localized data file "replace:" entry
    for (String nonComposedNumberValue : this.normalizeData.keySet()) {
      if (nonComposedNumberValue.contains(" ")) {
        String composedNumberValue = this.normalizeData.get(nonComposedNumberValue);
        numberSentence = numberSentence.replace(nonComposedNumberValue, composedNumberValue);
      }
    }
    
    return numberSentence.trim();
  }
  
  
  /**
   * Method to check false redundant input
   *
   * <br/> Note: call this after normalize (lemma,replace,...) text
   * 
   * @param int new_number, string[] words - looking for count of localized name of new_numerb in words
   * @throws NumberFormatException if redundant input error
   * @implNote this method has language configuration dependency
   * <br/> example 1: check_double_input (1000, "thousand thousand") with lang="en" throws a NumberFormatException
   * <br/> example 2: check_double_input (1000, "thousand thousand") with lang="de" its ok
   * <br/> example 3: check_double_input (1000, "tausend tausend") with lang="de" throws a NumberFormatException
   */
  protected void checkDoubleInput(Long newNumber, List<String> cleanNumbers) throws NumberFormatException {
    String localizedName =  this.getNameByNumberValue(newNumber);
    
    final boolean countGreaterOne = cleanNumbers.indexOf(localizedName) != cleanNumbers.lastIndexOf(localizedName);
    if (countGreaterOne)
        throw new NumberFormatException (String.format("Redundant number word %s in! Please enter a valid number word (eg. two million twenty three thousand and forty nine)",localizedName));
  }
  

  /**
   * Method to get the value for the measure aka 1000, 1_000_000 ...
   * @param measureIndex index of measure
   * @param cleanNumbers
   * @return multiplier for measure
   */
  protected long getMeasureMultiplier (int measureIndex, List<String> cleanNumbers) {
    List<String> param = cleanNumbers.subList(0,measureIndex);
    if (param.isEmpty()) {
      param.add(this.getNameByNumberValue(1L));
    }
    long multiplier = this.numberFormation(param);
    return multiplier;
  }

  /**
   * Method to get the localized name form value
   * @param newNumber numeric value
   * @return name from language configuration or <code>null</code> if not found 
   */
  protected String getNameByNumberValue (Long newNumber) {
    for (String key : this.filebasedNumberSystem.keySet()) {
      if (newNumber.equals(this.filebasedNumberSystem.get(key))) {
        return key;
      }
    }
    return null;
  }
  
  /**
   * Method to get the index of name for given number
   * 
   * <br/> note: call this after normalize (lemma,replace,...) text
   * 
   * @param newNumber number to looking for
   * @param cleanNumbers
   * @return index or -1 if not found
   */
  protected int getIndexForNumber (Long newNumber, List<String> cleanNumbers) {
    String localizedName = getNameByNumberValue(newNumber);
    return cleanNumbers.indexOf(localizedName);
  }
  
  /**
   * Method to get the pre-decimal number from clean_number
   * @param sorted list with number words
   * @return number
   */
  protected Long getNumberValue (List<String> cleanNumbers) {
    long result = 0L;

    /*
    * The simple algorithm based on the idea from NLP to work with tagging (key)words
    * but yes it is handmade implemented today.
    *
    * -- 2021-02-05 --
    * The tagging can be tested on for example https://parts-of-speech.info and tell for
    * nine trillion one billion two million twenty three thousand and forty nine point two three six nine
    * - "and" is a conjunction
    * - "point" is a none
    * - all other are numbers
    * But also contains this line these "measure words" for numbers:
    * - trillion
    * - billion
    * - million
    * - thousand
    * - hundred
    * This new algorithm split the word array from highest value to lowest 
    * (because hundred can be a measure and also a number). Then it work
    * only with number for this measure, simplify so the algorithm and
    * make it free from other measure part in the number.
    * Also it is no different to calculate a trillion or a million or other
    */
    
    for (Long measureValue : sortedMeasureValues){
      int measureValueIndex = getIndexForNumber(measureValue, cleanNumbers);
      if (measureValueIndex > -1){
        result +=  getMeasureMultiplier(measureValueIndex, cleanNumbers) * measureValue;
        cleanNumbers = cleanNumbers.subList(measureValueIndex+1,cleanNumbers.size());
      }
    }
    // Now we add the value of less then hundred
    if (cleanNumbers.size() > 0){
      int multiplier = numberFormation(cleanNumbers);
      result +=  multiplier * 1;
    }

    return result;
  }
}
