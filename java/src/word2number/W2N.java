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
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Locale;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * 
 * Word2Number implementation
 * 
 * This class implements an easy algorithm to translate number words to numbers from sentences.
 * It takes an <code>CharSequence</code> like <code>String</code>, <code>StringBuilder</code> or 
 * <code>StringBuffer</code> instances and returns as result <code>null</code> or an 
 * <code>Number</code> instance.
 * 
 * @author Sͬeͥbͭaͭsͤtͬian
 *
 */
public class W2N {
  
  private final HashMap<String, Object> filebasedNumberSystem;
  private final ArrayList<String> decimalWords;
  
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
      InputStream dataFile = this.getClass().getResourceAsStream("data/config_"+this.lang+".properties");
      BufferedReader numberSystemData = new BufferedReader( new InputStreamReader(new BufferedInputStream(dataFile,40960),"utf-8"));
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
            
          }
          else if (key.startsWith("measure:")) {
            
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
  
  public Number wordToNum (Number newNumberValue) {
    if (null == newNumberValue) // same as python
      throw new NumberFormatException("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");

    return newNumberValue;
  }
  
  /**
   * function to return integer for an input `number_sentence` string
   * @param numberSentence text
   * @return Number or null
   */
  public Number wordToNum (CharSequence newNumberSentence) {
    Number result = null;

    if (null == newNumberSentence) // same as python
      throw new NumberFormatException("Type of input is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')");

    // return the number if user enters a number string
    try { 
      return Integer.valueOf(newNumberSentence.toString()); // TODO: working with Long - now in same range as Python
    }
    catch (NumberFormatException noIntMaybeFloat) {
      try {
        return Double.valueOf(newNumberSentence.toString());
      }
      catch (NumberFormatException okMoreSpecificAlgorithmNeeded) {}
    }
    
    String numberSentence = newNumberSentence.toString();
    
    numberSentence = this.normalize(numberSentence);
    

    String [] splitWords = numberSentence.split("[\\s,]+"); // strip extra spaces and comma and than split sentence into words
    
    LinkedList<String> cleanNumbers = new LinkedList<>();
    LinkedList<String> cleanDecimalNumbers = new LinkedList<>();

    // removing and, & etc.
    for (String word : splitWords) {
      if (this.filebasedNumberSystem.containsKey(word)) {
        cleanNumbers.add(word);
      }
      else if (word.equals(this.filebasedNumberSystem.get("point"))){
        cleanNumbers.add(word);
      }
    }

    // Error message if the user enters invalid input!
    if (cleanNumbers.size()== 0) // TODO check what python do with None String
        throw new NumberFormatException("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");

    this.checkDoubleInput(cleanNumbers.stream().toArray(String[]::new));// Error if user enters million,billion, thousand or decimal point twice

    // separate decimal part of number (if exists)
    String point = this.filebasedNumberSystem.get("point").toString();
    boolean pointCount = cleanNumbers.indexOf(point)>-1;
    if (pointCount) {
      cleanDecimalNumbers = new LinkedList<>(cleanNumbers.subList(cleanNumbers.indexOf(point)+1, cleanNumbers.size()));
      cleanNumbers = new LinkedList<>(cleanNumbers.subList(0,cleanNumbers.indexOf(point)));
    }
    // special case "point" without pre or post number   // TODO check it really a number, bit for python compatibility it need to
    if (cleanDecimalNumbers.size() == 0 && cleanNumbers.size() == 0) return Integer.valueOf(0);

    int trillionIndex = getTrillionIndex(cleanNumbers);
    int billionIndex = getBillionIndex(cleanNumbers);
    int millionIndex = getMillionIndex(cleanNumbers);
    int thousandIndex = getThousandIndex(cleanNumbers);

    if ((thousandIndex > -1 && (thousandIndex < millionIndex || thousandIndex < billionIndex)) || (millionIndex > -1 && millionIndex < billionIndex))
      throw new NumberFormatException("Malformed number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");

    long totalSum = 0;  //# storing the number to be returned

    if (cleanNumbers.size() > 0) {
      // hack for now, better way todo
      if (cleanNumbers.size() == 1) {
        totalSum += Long.valueOf(this.filebasedNumberSystem.get(cleanNumbers.get(0)).toString()); // TODO: oh no hack
      }
      else {
        if (trillionIndex > -1) {
          int trillionMultiplier = numberFormation(cleanNumbers.subList(0,trillionIndex));
          totalSum += trillionMultiplier * 1000000000000L;
        }

        if (billionIndex > -1) {
          int billionMultiplier = 0;
          if (trillionIndex > -1) {
            billionMultiplier = numberFormation(cleanNumbers.subList(trillionIndex+1,billionIndex));
          }
          else {
            billionMultiplier = numberFormation(cleanNumbers.subList(0,billionIndex));
          }
          totalSum += billionMultiplier * 1000000000L;
        }

        if (millionIndex > -1) {
          int millionMultiplier = 0;
          if (billionIndex > -1) {
            millionMultiplier = numberFormation(cleanNumbers.subList(billionIndex+1,millionIndex));
          }
          else if (trillionIndex > -1 && billionIndex == -1) {
            millionMultiplier = numberFormation(cleanNumbers.subList(trillionIndex+1,millionIndex));
          }
          else {
            millionMultiplier = numberFormation(cleanNumbers.subList(0,millionIndex));
          }
          totalSum += millionMultiplier * 1000000;
        }

        if (thousandIndex > -1) {
          int thousandMultiplier = 0;
          if (millionIndex > -1) {
              thousandMultiplier = numberFormation(cleanNumbers.subList(millionIndex+1,thousandIndex));
          }
          else if (billionIndex > -1 && millionIndex == -1) {
              thousandMultiplier = numberFormation(cleanNumbers.subList(billionIndex+1,thousandIndex));
          }
          else if (trillionIndex > -1 && billionIndex > -1 && millionIndex == -1) {
            thousandMultiplier = numberFormation(cleanNumbers.subList(trillionIndex+1,thousandIndex));
          }
          else {
              thousandMultiplier = numberFormation(cleanNumbers.subList(0,thousandIndex));
          }
          totalSum += thousandMultiplier * 1000;
        }

        int hundreds = 0;
        if (thousandIndex > -1 && thousandIndex != cleanNumbers.size()-1) {
          hundreds = numberFormation(cleanNumbers.subList(thousandIndex+1, cleanNumbers.size()));
        }
        else if (millionIndex > -1 && millionIndex != cleanNumbers.size()-1 && thousandIndex != cleanNumbers.size()-1) {
          hundreds = numberFormation(cleanNumbers.subList(millionIndex+1,cleanNumbers.size()));
        }
        else if (billionIndex > -1 && billionIndex != cleanNumbers.size()-1 && thousandIndex != cleanNumbers.size()-1) {
          hundreds = numberFormation(cleanNumbers.subList(billionIndex+1,cleanNumbers.size()));
        }
        else if (thousandIndex == -1 && millionIndex == -1 && billionIndex == -1) {
          hundreds = numberFormation(cleanNumbers);
        }
        else {
          hundreds = 0;
        }
        totalSum += hundreds;
      }
      Long value = Long.valueOf(totalSum);
      result = value;
      if (value.longValue() < Long.valueOf(Integer.MAX_VALUE).longValue() &&
          value.longValue() > Long.valueOf(Integer.MIN_VALUE).longValue()) {
        result = Integer.valueOf(value.intValue());
      }
    }

    // adding decimal part to total_sum (if exists)
    if (cleanDecimalNumbers.size() > 0){
        String decimalSum = getDecimalString(cleanDecimalNumbers);
        decimalSum = ""+totalSum+"."+decimalSum;
        if (decimalSum.substring(decimalSum.indexOf(".")).equals(".0")) {
          decimalSum = decimalSum.substring(0, decimalSum.indexOf("."));
          Long value = Long.valueOf(decimalSum);
          result = value;
          if (value.longValue() < Long.valueOf(Integer.MAX_VALUE).longValue() &&
              value.longValue() > Long.valueOf(Integer.MIN_VALUE).longValue()) {
            result = Integer.valueOf(value.intValue());
          }
        }
        else {
          result = Double.valueOf(decimalSum);
        }
    }
    
    return result;
  }
  

  /**
   * function to normalize input text
   * @param numberSentence input string
   * @return normalized input
   */
  protected String normalize(String numberSentence) {
    if (new Locale(this.lang).getLanguage().equals(new Locale("fr").getLanguage())){
      // do not remove '-' but add minus
      numberSentence = numberSentence.replace("vingt et un", "vingt-et-un");
      numberSentence = numberSentence.replace("trente et un", "trente-et-un");
      numberSentence = numberSentence.replace("quarante et un", "quarante-et-un");
      numberSentence = numberSentence.replace("cinquante et un", "cinquante-et-un");
      numberSentence = numberSentence.replace("soixante et un", "soixante-et-un");
    }
    else{
      numberSentence = numberSentence.replace("-", " ");
    }
    numberSentence = numberSentence.toLowerCase(new Locale(this.lang));  // converting input to lowercase
    return numberSentence.trim();
  }
  
  
  /**
   * function to check false redundant input 
   * @param cleanNumbers array of number words
   * @throws NumberFormatException if redundant input error
   */
  protected void checkDoubleInput(String ... cleanNumbers) throws NumberFormatException {
    // special map returns zero if key isn't included
    HashMap<String,Long> howMuch = new HashMap<>(Stream.of(cleanNumbers).collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))) {
      private static final long serialVersionUID = 1L;
      @Override
      public Long get(Object key) {
        return null == super.get(key) ? Long.valueOf(0) : super.get(key);
      }
    };
    
    if (new Locale(this.lang).getLanguage().equals(new Locale("de").getLanguage())) {
      if (howMuch.get("tausend") > 1 || howMuch.get("million") > 1 || howMuch.get("milliarde") > 1 || howMuch.get("billion") > 1 || howMuch.get("komma") > 1)
        throw new NumberFormatException ("Redundantes Nummernwort! Bitte gebe ein zulässiges Nummernwort ein (z.B. zwei Millionen Dreiundzwanzigtausend und Neunundvierzig)");
    }
    else if (new Locale(this.lang).getLanguage().equals(new Locale("fr").getLanguage())) {
      if (howMuch.get("mille") > 1 || howMuch.get("million") > 1 || howMuch.get("milliard") > 1 || howMuch.get("billion") > 1 || howMuch.get("point") > 1)
        throw new NumberFormatException ("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
    }
    else if (new Locale(this.lang).getLanguage().equals(new Locale("hi").getLanguage())){
    }
    else if (new Locale(this.lang).getLanguage().equals(new Locale("pt").getLanguage())) {
      if (howMuch.get("mil") > 1 || howMuch.get("milhão") > 1 || howMuch.get("bilhão") > 1 || howMuch.get("point") > 1)
        throw new NumberFormatException ("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
    }
    else if (new Locale(this.lang).getLanguage().equals(new Locale("ru").getLanguage())) {
      if (howMuch.get("тысяча") > 1 || howMuch.get("миллион") > 1 || howMuch.get("миллиард") > 1 || howMuch.get("целых") > 1 || howMuch.get("целая") > 1)
        throw new NumberFormatException ("Избыточное числовое слово! Введите правильное числовое слово (например, два миллиона двадцать три тысячи сорок девять)");
    }
    else if (new Locale(this.lang).getLanguage().equals(new Locale("en").getLanguage())) {
      // Error if user enters million,billion, thousand or decimal point twice
      if (howMuch.get("thousand") > 1 || howMuch.get("million") > 1 || howMuch.get("billion") > 1 || howMuch.get("point") > 1)
          throw new NumberFormatException ("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
    }
    else { // fallback => en
      // Error if user enters million,billion, thousand or decimal point twice
      if (howMuch.get("thousand") > 1 || howMuch.get("million") > 1 || howMuch.get("billion") > 1 || howMuch.get("point") > 1)
          throw new NumberFormatException ("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)");
    }
  }
  
  /**
   * Constant to descripe a looking for has no result
   */
  protected final int NOT_FOUND = -1;
  /**
   * function to get billion index
   * @param cleanNumbers number array
   * @return index or -1 if not found
   * @see NOT_FOUND
   */
  protected int getBillionIndex(List<String> cleanNumbers) {
    int index = NOT_FOUND;
    switch (this.lang) {
      case "de":
        index = cleanNumbers.indexOf("milliarde");
        if (index == NOT_FOUND) index = cleanNumbers.indexOf("milliarden");
        break;
      case "fr":
        index = cleanNumbers.indexOf("milliard");
        break;
      case "hi":
        break;
      case "pt":
        index = cleanNumbers.indexOf("bilhão");
        break;
      case "ru":
        index = cleanNumbers.indexOf("миллиард");
        if (index == NOT_FOUND) index = cleanNumbers.indexOf("миллиарда");
        break;
      case "en":
      default:
        index = cleanNumbers.indexOf("billion");
        break;
    }
      return index;
  }
  /**
   * function to get billion index
   * @param cleanNumbers number array
   * @return index or -1 if not found
   * @see NOT_FOUND
   */
  protected int getTrillionIndex(List<String> cleanNumbers) {
    int index = NOT_FOUND;
    switch (this.lang) {
      case "de":
        index = cleanNumbers.indexOf("billion");
        if (index == NOT_FOUND) index = cleanNumbers.indexOf("billionen");
        break;
      case "fr":
        index = cleanNumbers.indexOf("billion");
        break;
      case "hi":
        break;
      case "pt":
        index = cleanNumbers.indexOf("trilhão");
        break;
      case "ru":
        index = cleanNumbers.indexOf("триллион");
        break;
      case "en":
      default:
        index = cleanNumbers.indexOf("trillion");
        break;
    }
      return index;
  }

  /**
   * function to get million index
   * @param cleanNumbers number array
   * @return index or -1 if not found
   */
  protected int getMillionIndex(List<String> cleanNumbers) {
    int index = NOT_FOUND;
    switch (this.lang) {
      case "de":
        index = cleanNumbers.indexOf("million");
        if (index == NOT_FOUND) index = cleanNumbers.indexOf("millionen");
        break;
      case "hi":
        break;
      case "pt":
        index = cleanNumbers.indexOf("milhão");
        break;
      case "ru":
        index = cleanNumbers.indexOf("миллион");
        if (index == NOT_FOUND) index = cleanNumbers.indexOf("миллиона");
        break;
      case "fr":
      case "en":
      default:
        index = cleanNumbers.indexOf("million");
        break;
    }
    return index;
  }

  /**
   * function to get thousand index
   * @param cleanNumbers number array
   * @return index or -1 if not found
   */
  protected int getThousandIndex(List<String> cleanNumbers) {
    int index = NOT_FOUND;
    switch (this.lang) {
      case "de":
        index = cleanNumbers.indexOf("tausend");
        break;
      case "fr":
        index = cleanNumbers.indexOf("mille");
        break;
      case "hi":
        break;
      case "pt":
        index = cleanNumbers.indexOf("mil");
        break;
      case "ru":
        index = cleanNumbers.indexOf("тысяча");
        if (index == NOT_FOUND) index = cleanNumbers.indexOf("тысячи");
        break;
      case "en":
      default:
        index = cleanNumbers.indexOf("thousand");
        break;
    }
    return index;
  }


}
