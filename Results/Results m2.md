Collections 

[+] Found dataset pair for system version: collections-3.2.1 

 

--- Sample of combined Class Metrics for collections-3.2.1 --- 

     System           Version                     Class  PMD_Violations  Designite_Smells 

collections collections-3.2.1 AbstractTestSortedBidiMap             215                32 

collections collections-3.2.1       TestCollectionUtils             131               142 

collections collections-3.2.1      TestDoubleOrderedMap             108               163 

collections collections-3.2.1        TestPredicateUtils             108                48 

collections collections-3.2.1          AbstractTestList              96                75 

collections collections-3.2.1         TestIteratorUtils              88                92 

collections collections-3.2.1              TestMapUtils              83                64 

collections collections-3.2.1           AbstractTestMap              82                40 

collections collections-3.2.1  TestCursorableLinkedList              81               160 

collections collections-3.2.1           TestMultiKeyMap              76               174 

 

================ [collections-3.2.1 Analysis] ================ 

Total Classes Evaluated: 393 

Spearman Correlation Coefficient: 0.3703 

P-value (Significance level): 3.199827960899293e-14 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

 

 

################################################## 

###       GLOBAL CROSS-SYSTEM STATS PREVIEW    ### 

################################################## 

     System           Version                     Class  PMD_Violations  Designite_Smells 

collections collections-3.2.1 AbstractTestSortedBidiMap             215                32 

collections collections-3.2.1       TestCollectionUtils             131               142 

collections collections-3.2.1      TestDoubleOrderedMap             108               163 

collections collections-3.2.1        TestPredicateUtils             108                48 

collections collections-3.2.1          AbstractTestList              96                75 

collections collections-3.2.1         TestIteratorUtils              88                92 

collections collections-3.2.1              TestMapUtils              83                64 

collections collections-3.2.1           AbstractTestMap              82                40 

collections collections-3.2.1  TestCursorableLinkedList              81               160 

collections collections-3.2.1           TestMultiKeyMap              76               174 

collections collections-3.2.1           AbstractTestBag              65                33 

collections collections-3.2.1    AbstractTestCollection              65                65 

collections collections-3.2.1   TestObjectGraphIterator              59                27 

collections collections-3.2.1             FastArrayList              55                 3 

collections collections-3.2.1                  Flat3Map              53                59 

 

================ [COMBINED SYSTEM-WIDE GLOBAL Analysis] ================ 

Total Classes Evaluated: 393 

Spearman Correlation Coefficient: 0.3703 

P-value (Significance level): 3.199827960899293e-14 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

Ant 

 

################################################## 

###          COMBINED METRICS LEADERBOARD      ### 

################################################## 

System                   Class  PMD_Violations  Designite_Smells 

   ant      CBZip2OutputStream              88               193 

   ant                    Main              68                15 

   ant        DirectoryScanner              62                23 

   ant                 Project              59                 9 

   ant     IntrospectionHelper              56                44 

   ant               BlockSort              55               133 

   ant          MSVSSConstants              48                 0 

   ant IntrospectionHelperTest              44                46 

   ant                NetRexxC              44                 8 

   ant       CBZip2InputStream              41                79 

   ant                     Zip              41                31 

   ant                  Delete              40                14 

   ant         AbstractFileSet              38                 0 

   ant           ResourceUtils              37                19 

   ant                 Javadoc              36                17 

  

================ [ant Analysis] ================ 

Total Classes Evaluated: 1264 

Spearman Correlation Coefficient: 0.2012 

P-value (Significance level): 5.18229096414267e-13 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

  

donag@G-pc MINGW64 ~/OneDrive/Desktop/QC/QualitasCorpus-20130901r/Systems/ant (main) 

$ cd ./ 

  

donag@G-pc MINGW64 ~/OneDrive/Desktop/QC/QualitasCorpus-20130901r/Systems/ant (main) 

$ cd ../ 

  

donag@G-pc MINGW64 ~/OneDrive/Desktop/QC/QualitasCorpus-20130901r/Systems (main) 

$ cd antlr 

  

donag@G-pc MINGW64 ~/OneDrive/Desktop/QC/QualitasCorpus-20130901r/Systems/antlr (main) 

$ ls 

antlr-4.0/  Bash.sh*  Calc_p_value.py  DesigniteJava.jar  projectList.txt 

  

donag@G-pc MINGW64 ~/OneDrive/Desktop/QC/QualitasCorpus-20130901r/Systems/antlr (main) 

$ ./Bash.sh 

================================================== 

🚀 Processing project: antlr-4.0 

================================================== 

🔍 Running PMD analysis... 

Nov 01, 2026 3:20:10 P.M. net.sourceforge.pmd.PMD encourageToUseIncrementalAnalysis 

WARNING: This analysis could be faster, please consider using Incremental Analysis: https://pmd.github.io/pmd-6.23.0/pmd_userdocs_incremental_analysis.html 

✅ PMD completed. Saved to: antlr-4.0_PMD_RULESET.xml 

📐 Running Designite analysis... 

Parsing the source code ... 

Resolving symbols... 

Extracting metrics... 

Extracting code smells... 

Done. 

✅ Designite completed. Saved to folder: antlr-4.0_Designite_Output/ 

  

donag@G-pc MINGW64 ~/OneDrive/Desktop/QC/QualitasCorpus-20130901r/Systems/antlr (main) 

$ python Calc_p_value.py 

Scanning base directory: C:\Users\donag\OneDrive\Desktop\QC\QualitasCorpus-20130901r\Systems\antlr 

  

[+] Detected localized project workspace: antlr 

  

  

################################################## 

###          COMBINED METRICS LEADERBOARD      ### 

################################################## 

System                 Class  PMD_Violations  Designite_Smells 

antlr        TestGraphNodes             166               144 

antlr TestActionTranslation             158                 6 

antlr      TestASTStructure              82                96 

antlr     PredictionContext              61                12 

antlr              BaseTest              58                24 

antlr    ParserATNSimulator              58                40 

antlr       TestIntervalSet              52               342 

antlr               Grammar              36                12 

antlr       TestParseErrors              36                22 

antlr           IntervalSet              35                 6 

antlr                  Tool              32                 8 

antlr            TestJavaLR              32                10 

antlr        Array2DHashSet              29                 6 

antlr       TestPerformance              28                60 

antlr TestCommonTokenStream              28                44 

  

================ [antlr Analysis] ================ 

Total Classes Evaluated: 269 

Spearman Correlation Coefficient: 0.3627 

P-value (Significance level): 8.748248006941111e-10 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

Antlr 

################################################## 

###          COMBINED METRICS LEADERBOARD      ### 

################################################## 

System                 Class  PMD_Violations  Designite_Smells 

antlr        TestGraphNodes             166               144 

antlr TestActionTranslation             158                 6 

antlr      TestASTStructure              82                96 

antlr     PredictionContext              61                12 

antlr              BaseTest              58                24 

antlr    ParserATNSimulator              58                40 

antlr       TestIntervalSet              52               342 

antlr               Grammar              36                12 

antlr       TestParseErrors              36                22 

antlr           IntervalSet              35                 6 

antlr                  Tool              32                 8 

antlr            TestJavaLR              32                10 

antlr        Array2DHashSet              29                 6 

antlr       TestPerformance              28                60 

antlr TestCommonTokenStream              28                44 

  

================ [antlr Analysis] ================ 

Total Classes Evaluated: 269 

Spearman Correlation Coefficient: 0.3627 

P-value (Significance level): 8.748248006941111e-10 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

 

Aoi 

[+] Detected localized project workspace: aoi 

  

  

################################################## 

###          COMBINED METRICS LEADERBOARD      ### 

################################################## 

System                  Class  PMD_Violations  Designite_Smells 

   aoi           LayoutWindow             433               341 

   aoi           TriangleMesh             398               326 

   aoi    TriMeshEditorWindow             388               203 

   aoi              Raytracer             309               226 

   aoi                 Raster             293               361 

   aoi            CSGModeller             240                99 

   aoi        ProcedureEditor             221                54 

   aoi SplineMeshEditorWindow             201                97 

   aoi   SoftwareCanvasDrawer             197               332 

   aoi             SplineMesh             191                94 

   aoi       MeshEditorWindow             182               145 

   aoi         TriMeshBeveler             181               136 

   aoi          IconGenerator             152               346 

   aoi              PhotonMap             144               121 

   aoi                  Scene             142                32 

  

================ [aoi Analysis] ================ 

Total Classes Evaluated: 653 

Spearman Correlation Coefficient: 0.6013 

P-value (Significance level): 1.8577106409400513e-65 

-------------------------------------------------- 

Interpretation: Strong Positive Correlation! Badly formatted modules cleanly align with severe structural decay. 

================================================== 

 

Argouml 

(due to size unable to properly get all smells) 

[+] Detected localized project workspace: argouml 

  

  

################################################## 

###          COMBINED METRICS LEADERBOARD      ### 

################################################## 

System                       Class  PMD_Violations  Designite_Smells 

argouml                   CPPParser             820               553 

argouml                    CPPLexer             635               284 

argouml                GeneratorCpp             195                85 

argouml              STDCTokenTypes             155                 0 

argouml ModelAccessModelInterpreter             143                12 

argouml                      Parser             105                83 

argouml                    Verbatim              79                36 

argouml                     Project              72                 0 

argouml               GeneratorPHP4              64                32 

argouml             GeneratorCSharp              59                26 

argouml          UserDefinedProfile              53                 6 

argouml               GeneratorJava              48                48 

argouml                    Modeller              48                53 

argouml                     Modeler              47                38 

argouml                        Text              46                 4 

  

================ [argouml Analysis] ================ 

Total Classes Evaluated: 1307 

Spearman Correlation Coefficient: 0.1818 

P-value (Significance level): 3.525821379003731e-11 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

Aspectj 

Known error in pmd version came up: 

java.lang.NullPointerException: Cannot invoke "net.sourceforge.pmd.lang.java.ast.ASTClassOrInterfaceType.hasImageEqualTo(String)" because "type" is null 

        at net.sourceforge.pmd.lang.java.rule.errorprone.ProperCloneImplementationRule.blockHasAllocations(ProperCloneImplementationRule.java:46) 

        at net.sourceforge.pmd.lang.java.rule.errorprone.ProperCloneImplementationRule.visit(ProperCloneImplementationRule.java:35) 

        at net.sourceforge.pmd.lang.java.ast.ASTMethodDeclaration.jjtAccept(ASTMethodDeclaration.java:37) 

        at net.sourceforge.pmd.lang.java.rule.JavaRuleChainVisitor.visit(JavaRuleChainVisitor.java:44) 

        at net.sourceforge.pmd.lang.rule.AbstractRuleChainVisitor.visitAll(AbstractRuleChainVisitor.java:96) 

        at net.sourceforge.pmd.RuleChain.apply(RuleChain.java:67) 

        at net.sourceforge.pmd.RuleSets.apply(RuleSets.java:140) 

        at net.sourceforge.pmd.SourceCodeProcessor.processSource(SourceCodeProcessor.java:194) 

        at net.sourceforge.pmd.SourceCodeProcessor.processSourceCodeWithoutCache(SourceCodeProcessor.java:107) 

        at net.sourceforge.pmd.SourceCodeProcessor.processSourceCode(SourceCodeProcessor.java:89) 

        at net.sourceforge.pmd.SourceCodeProcessor.processSourceCode(SourceCodeProcessor.java:51) 

        at net.sourceforge.pmd.processor.PmdRunnable.call(PmdRunnable.java:78) 

        at net.sourceforge.pmd.processor.PmdRunnable.call(PmdRunnable.java:24) 

        at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264) 

        at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:539) 

        at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264) 

        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136) 

        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635) 

        at java.base/java.lang.Thread.run(Thread.java:840) 

 

 

results 

 

[+] Detected localized project workspace: aspectj 

  

  

################################################## 

###          COMBINED METRICS LEADERBOARD      ### 

################################################## 

System                      Class  PMD_Violations  Designite_Smells 

aspectj              PublicScanner             793               372 

aspectj TheOriginalJDTScannerClass             793               372 

aspectj                  Constants             749                 0 

aspectj                 CodeStream             646               595 

aspectj           CompletionEngine             514               479 

aspectj                      Scope             415               224 

aspectj                    Opcodes             402                 0 

aspectj                       Main             375               259 

aspectj              CharOperation             339                56 

aspectj               ASTConverter             319               306 

aspectj       InstructionConstants             304                 1 

aspectj  TheOriginalJDTParserClass             271               383 

aspectj                    TypeIds             248                 0 

aspectj     DefaultBytecodeVisitor             224               144 

aspectj           JavaModelManager             222               142 

  

================ [aspectj Analysis] ================ 

Total Classes Evaluated: 1750 

Spearman Correlation Coefficient: 0.4693 

P-value (Significance level): 1.5214904766760475e-96 

-------------------------------------------------- 

Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes. 

================================================== 

 
