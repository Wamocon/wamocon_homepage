$f = "c:\Users\Leon Moretz\Documents\wamocon_homepage-4\page69503661.html"
$c = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

# Items to shift by 130px (CSS top values in artboard rec1051638191)
# Format: old CSS fragment -> new CSS fragment (only unique strings)
$shifts = @(
    # Softwareentwicklung title (1730300735317)
    @("1730300735317""{color:#ffffff;z-index:4;top:300px;", "1730300735317""{color:#ffffff;z-index:4;top:430px;"),
    # Softwareentwicklung desc (1730300735330) top:301
    @("1730300735330""{color:#ffffff;z-index:5;top:301px;", "1730300735330""{color:#ffffff;z-index:5;top:431px;"),
    # Divider 1 (1730365699782) top:387
    @("1730365699782""]{z-index:12;top:387px;", "1730365699782""]{z-index:12;top:517px;"),
    # Moderne Technologien title (1730365545117) top:416
    @("1730365545117""{color:#ffffff;z-index:8;top:416px;", "1730365545117""{color:#ffffff;z-index:8;top:546px;"),
    # Moderne Technologien desc (1730365545123) top:416
    @("1730365545123""{color:#ffffff;z-index:9;top:416px;", "1730365545123""{color:#ffffff;z-index:9;top:546px;"),
    # Projektarbeit title (1730365565500) top:549
    @("1730365565500""{color:#ffffff;z-index:10;top:549px;", "1730365565500""{color:#ffffff;z-index:10;top:679px;"),
    # Projektarbeit desc (1730365565506) top:549
    @("1730365565506""{color:#ffffff;z-index:11;top:549px;", "1730365565506""{color:#ffffff;z-index:11;top:679px;"),
    # Divider 2 (1749324247325) top:621
    @("1749324247325""]{z-index:13;top:621px;", "1749324247325""]{z-index:13;top:751px;"),
    # Qualitaetssicherung desc (1748003702037) top:665
    @("1748003702037""{color:#ffffff;z-index:18;top:665px;", "1748003702037""{color:#ffffff;z-index:18;top:795px;"),
    # Qualitaetssicherung title (1748003702034) top:665
    @("1748003702034""{color:#ffffff;z-index:19;top:665px;", "1748003702034""{color:#ffffff;z-index:19;top:795px;"),
    # Divider 3 (1749324143622) top:744
    @("1749324143622""]{z-index:17;top:744px;", "1749324143622""]{z-index:17;top:874px;"),
    # Datenbanken title (1748003718728) top:777
    @("1748003718728""{color:#ffffff;z-index:20;top:777px;", "1748003718728""{color:#ffffff;z-index:20;top:907px;"),
    # Datenbanken desc (1748003718725) top:777
    @("1748003718725""{color:#ffffff;z-index:21;top:777px;", "1748003718725""{color:#ffffff;z-index:21;top:907px;"),
    # Divider 4 (1749324186080) top:841
    @("1749324186080""]{z-index:16;top:841px;", "1749324186080""]{z-index:16;top:971px;"),
    # Problembehebung title (1748003721831) top:882
    @("1748003721831""{color:#ffffff;z-index:22;top:882px;", "1748003721831""{color:#ffffff;z-index:22;top:1012px;"),
    # Problembehebung desc (1749324295476) top:892
    @("1749324295476""{color:#ffffff;z-index:23;top:892px;", "1749324295476""{color:#ffffff;z-index:23;top:1022px;"),
    # Divider 5 (1749324522817) top:960
    @("1749324522817""]{z-index:14;top:960px;", "1749324522817""]{z-index:14;top:1090px;"),
    # Highlight Projekt desc (1748003735227) top:1029
    @("1748003735227""{color:#ffffff;z-index:24;top:1029px;", "1748003735227""{color:#ffffff;z-index:24;top:1159px;"),
    # Highlight Projekt title (1748003735224) top:1000
    @("1748003735224""]{color:#ffffff;text-align:center;z-index:25;top:1000px;", "1748003735224""]{color:#ffffff;text-align:center;z-index:25;top:1130px;")
)

$count = 0
foreach ($s in $shifts) {
    if ($c.Contains($s[0])) {
        $c = $c.Replace($s[0], $s[1])
        $count++
    } else {
        Write-Output "NOT FOUND: $($s[0].Substring(0, 40))"
    }
}
Write-Output "Replaced: $count of $($shifts.Count)"
