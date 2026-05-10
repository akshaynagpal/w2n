using Gee;

class word2number.W2N : GLib.Object {

    static string data_source;

    string lang = "";
    HashMap<string, long> numberSystem;
    ArrayList<string> decimalWords;
    HashMap<string,string> normalizeData;
    ArrayList<long> sortedMeasureValues;
    string localizedPointName = "";


    public W2N (string? langParam = null) {
        string newLang = (langParam ?? 
            GLib.Environment.get_variable("w2n.lang") ??
            GLib.Environment.get_variable("LANGUAGE") ??
            "en"); // fallback
        this.lang = newLang.substring(0,2);
        

        this.numberSystem = new HashMap<string, long>();
        this.decimalWords = new ArrayList<string>();
        this.normalizeData = new HashMap<string, string>();
        this.sortedMeasureValues = new ArrayList<long>();
    
        string config;
        try {
            FileUtils.get_contents (data_source+"data/config_"+this.lang+".properties", out config);
        }
        catch (FileError ignore) {
            config="";
        }
        string [] lines = Regex.split_simple("[\n\r]", config.strip());

        int zeroToNine = 0;

        foreach (string line in lines) {
            if (line[0]=='#') {
            }
            else {
                string [] keyValue = line.split ("=",2);
                string key = keyValue [0].strip();
                string value = keyValue [1].strip();
                const string REPLACE = "replace:";
                const string MEASURE = "measure:";
                if (key.length >= REPLACE.length && REPLACE == key.slice(0,8)) {
                    key = key.substring(REPLACE.length);
                    this.normalizeData[key]=value;
                }
                else if (key.length >= MEASURE.length && MEASURE == key.slice(0,8)) {
                    key = key.substring(MEASURE.length);
                    long number = long.parse (value+"\0");  
                    this.sortedMeasureValues.add (number);
                }
                else if (key == "point") {
                    this.localizedPointName = value;
                }
                else {
                    long number = long.parse (value+"\0");
                    this.numberSystem[key] = number;
                }
                if (zeroToNine<10) {
                    this.decimalWords.add (key);
                    zeroToNine++;
                }
            }
        }
        sortedMeasureValues.sort ((a, b) => {
            return a > b ? -1 : 1;
        });
    }

    
    public static int main(string[] args) {
        W2N.data_source = args[0].substring(0,(args[0].char_count() - "W2N".char_count()));

        stdout.printf("Hello, World\n");

        W2N instance = new W2N();

        return 0;
    }
}