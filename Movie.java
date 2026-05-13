public static class RatingMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] cols = value.toString().split(",");
        if (key.get() == 0) return; // Skip header
        
        // ratings.csv: UserID[0], MovieID[1], Rating[2]
        String userId = cols[0];
        double rating = Double.parseDouble(cols[2]);
        context.write(new Text(userId), new DoubleWritable(rating));
    }
}

public static class StatsReducer extends Reducer<Text, DoubleWritable, Text, Text> {
    public void reduce(Text key, Iterable<DoubleWritable> values, Context context) throws IOException, InterruptedException {
        double sum = 0, min = 5.1, max = 0;
        int count = 0;
        for (DoubleWritable val : values) {
            double r = val.get();
            sum += r;
            if (r < min) min = r;
            if (r > max) max = r;
            count++;
        }
        double avg = sum / count;
        String result = "Max: " + max + " Min: " + min + " Avg: " + avg;
        context.write(key, new Text(result));
    }
}