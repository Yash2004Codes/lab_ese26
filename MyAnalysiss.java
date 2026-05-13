import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MyAnalysiss {

    // ---------------------------------------------------------
    // 1. MAPPER: Extracts the data you need
    // ---------------------------------------------------------
    public static class MyMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            
            // Skip the header row (very important!)
            if (key.get() == 0) return;

            String line = value.toString();
            String[] columns = line.split(","); // CHANGE: Change "," to "\t" if tab-separated

            try {
                // PLACEHOLDER: Choose your Key and Value columns
                // Example: If column 0 is 'Category' and column 2 is 'Price'
                String keyColumn = columns[0]; 
                double valueColumn = Double.parseDouble(columns[2]); 

                context.write(new Text(keyColumn), new DoubleWritable(valueColumn));
            } catch (Exception e) {
                // This prevents the whole program from crashing if a row is messy
            }
        }
    }

    // ---------------------------------------------------------
    // 2. REDUCER: Performs the math (Sum, Avg, Max, or Count)
    // ---------------------------------------------------------
    public static class MyReducer extends Reducer<Text, DoubleWritable, Text, Text> {
        public void reduce(Text key, Iterable<DoubleWritable> values, Context context) throws IOException, InterruptedException {
            
            double sum = 0;
            int count = 0;
            double max = 0;

            for (DoubleWritable val : values) {
                double currentVal = val.get();
                
                sum += currentVal;       // For Total
                count++;                 // For Count
                if(currentVal > max) max = currentVal; // For Max
            }

            double avg = sum / count;    // For Average

            // PLACEHOLDER: Choose what to output
            // Option A: Just the sum
            // context.write(key, new Text("Total: " + sum));
            
            // Option B: All stats (Common in exams)
            String result = "Sum: " + sum + " Avg: " + avg + " Max: " + max;
            context.write(key, new Text(result));
        }
    }

    // ---------------------------------------------------------
    // 3. DRIVER: The setup
    // ---------------------------------------------------------
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Exam Analysis");
        
        job.setJarByClass(MyAnalysis.class);
        job.setMapperClass(MyMapper.class);
        job.setReducerClass(MyReducer.class);

        // Define Mapper output types
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(DoubleWritable.class);

        // Define Final output types
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        // Paths from command line arguments
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}

/*
Reminder: Running the code
Compile: javac -classpath $(hadoop classpath) -d . MyAnalysis.java

Jar: jar -cvf analysis.jar *.class

Run: hadoop jar analysis.jar MyAnalysis /input /output


*/