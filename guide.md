start-all.sh or start-dfs.sh and then start-yarn.sh

jps
    ```
    **Expected Output:** You must see `NameNode`, `DataNode`, `ResourceManager`, and `NodeManager`. If you don't see these, your code won't run.

---

### 2. Prepare the HDFS Workspace
Hadoop lives in its own virtual file system. You need to create a place for your data.



*   **Create Input Directory:**
    ```bash
    hadoop fs -mkdir -p /user/admin/input
    ```
*   **Upload your Dataset (from Ubuntu to HDFS):**
    
```bash
    # Syntax: hadoop fs -put [LocalPath] [HDFSPath]
    hadoop fs -put ~/Downloads/movie_data.csv /user/admin/input
    ```
*   **Verify the file is there:**
    
```bash
    hadoop fs -ls /user/admin/input
    ```

---

### 3. The "Compile & Jar" Flow (The Coding Setup)
Assuming your code is in `MyAnalysis.java`, follow these exact steps to turn it into a runnable program:

hadoop classpath - to know the hadoop classpath

*   **Clean up old classes (Optional but safe):**
    ```bash
    rm *.class
    ```
*   **Compile with Hadoop Classpath:**
    
```bash
    javac -classpath $(hadoop classpath) -d . MyAnalysis.java
    ```
*   **Create the JAR file:**
    ```bash
    jar -cvf analysis.jar *.class
    ```

---

### 4. Execute the Job
This is the moment of truth. You are telling Hadoop to take your JAR, use the `MyAnalysis` class, and process the input.

*   **Run the Job:**
    ```bash
    hadoop jar analysis.jar MyAnalysis /user/admin/input /user/admin/output
    ```
    > **CRITICAL:** If the `/user/admin/output` folder already exists, the job will fail. Delete it first if you are re-running: `hadoop fs -rm -r /user/admin/output`.

---

### 5. Inspect the Results
Once the job hits 100%, check what you found.

*   **List the output files:**
    ```bash
    hadoop fs -ls /user/admin/output
    ```
*   **Read the actual results:**
    ```bash
    hadoop fs -cat /user/admin/output/part-r-00000
    ```
*   **Save to Local PC (for your Git push later):**
    
```bash
    hadoop fs -get /user/admin/output/part-r-00000 ./final_results.txt
    ```

### Troubleshooting "Emergency" Checklist:
*   **Safe Mode:** If Hadoop says "NameNode is in safe mode," run:
    `hadoop dfsadmin -safemode leave`
*   **Format NameNode:** Only do this as a **last resort** if nothing starts:
    `hdfs namenode -format` (This deletes all data in HDFS).
*   **Connection Refused:** This usually means you forgot to run `start-all.sh`.

You are set! Go clone your code, move the data, and start analyzing. Good luck!