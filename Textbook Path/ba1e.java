
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class clumps {

    public static void main(String[] args) throws FileNotFoundException {
        // Scan the input file input
        String input = args[0];
        File file = new File(input);

        Scanner scan = new Scanner(file);

        String genome = scan.next();

        
        int k = scan.nextInt();
        int L = scan.nextInt();
        int t = scan.nextInt();
        System.out.println(genome + " " + k + " " + L + " " + t);
        
        String text;
        Set<String> set = new HashSet<String>();
        double power = Math.pow(4, k);
        int pow = (int) power - 1;
        int[] Clump = new int[pow];
        int[] FrequencyArray = new int[pow];
        for (int i = 0; i < pow; i++) {
            Clump[i] = 0;
        }
        for (int i = 0; i < genome.length() - L; i++) {
            text = genome.substring(i, i + L);
            FrequencyArray = ComputingFrequencies(text, k);
           
            for (int index = 0; index < pow; index++) {
                
                if (FrequencyArray[index] >= t) {
                    Clump[index] = 1;
                }
            }
        }
        for (int i = 0; i < pow; i++) {
            if (Clump[i] == 1) {
                String pattern = NumberToPattern(i, k);
                set.add(pattern);
            }
        }
        if (set.size() == 0) {
            set.add("A");
            set.add("C");
            set.add("T");
            set.add("G");
        }

        System.out.println(set.toString());

    }

 
    public static int[] ComputingFrequencies(String text, int k) {
        

        String pattern;
        int j;
        double power = Math.pow(4, k);
        int pow = (int) power;
        int[] freq = new int[pow];
        for (int i = 0; i < pow - 1; i++) {
            freq[i] = 0;
        }
        for (int i = 0; i < (text.length()) - k; i++) {

            
            pattern = text.substring(i, i + k);

            j = PatternToNumber(pattern);

            freq[j] = freq[j] + 1;

        }

        return freq;
    }

    static int PatternToNumber(String pattern) {
        String symbol, Prefix;
        if (pattern.length() == 0) {
            return 0;
        }
        symbol = pattern.substring(pattern.length() - 1);
        Prefix = pattern.substring(0, pattern.length() - 1);
        int pre = PatternToNumber(Prefix);
        int num = SymbolToNumber(symbol);
        int ret = 4 * pre + num;
        return ret;

    }

    static int SymbolToNumber(String symbol) {
        int ret;
        if (symbol.equals("A")) {
            ret = 0;
        } else if (symbol.equals("C")) {
            ret = 1;
        } else if (symbol.equals("G")) {
            ret = 2;
        } else {
            ret = 3;
        }
        
        return ret;
    }

    static String NumberToPattern(int index, int k) {
       
        if (k == 1) {
            return NumberToSymbol(index);
        }

        int prefixIndex = index / 4;
        int r = index % 4;
        String symbol = NumberToSymbol(r);
        String PrefixPattern = NumberToPattern(prefixIndex, k - 1);
        return PrefixPattern + symbol;

    }

    static String NumberToSymbol(int index) {

        if (index == 0) {
            return "A";
        } else if (index == 1) {
            return "C";
        } else if (index == 2) {
            return "G";
        } else {
            return "T";
        }

    }

}
