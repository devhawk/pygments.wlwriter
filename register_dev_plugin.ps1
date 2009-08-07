$p = resolve-path Pygments.WLWriter\bin\Debug\Pygments.WLWriter.dll
new-itemproperty -path "HKCU:\Software\Microsoft\Windows Live\Writer\PluginAssemblies" -name "Pygments.WLWriter.Dev" -value $p
