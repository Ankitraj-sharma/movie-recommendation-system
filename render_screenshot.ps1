Add-Type -AssemblyName System.Drawing

$text = [System.IO.File]::ReadAllText("execution_output.txt", [System.Text.Encoding]::UTF8)
$lines = $text -split "`r?`n"

# Terminal font and measurements
$fontName = "Consolas"
$fontSize = 14
$font = New-Object System.Drawing.Font($fontName, $fontSize, [System.Drawing.FontStyle]::Regular)
$titleFont = New-Object System.Drawing.Font($fontName, 12, [System.Drawing.FontStyle]::Bold)

# Measure dimensions
$tempBmp = New-Object System.Drawing.Bitmap 1, 1
$tempG = [System.Drawing.Graphics]::FromImage($tempBmp)
$lineHeight = [int]($font.GetHeight($tempG) + 3)
$maxWidth = 0
foreach ($line in $lines) {
    $size = $tempG.MeasureString($line, $font)
    if ($size.Width -gt $maxWidth) { $maxWidth = [int]$size.Width }
}
$tempG.Dispose()
$tempBmp.Dispose()

$padding = 30
$titleBarHeight = 45
$width = [Math]::Max($maxWidth + ($padding * 2), 850)
$height = $titleBarHeight + ($lines.Length * $lineHeight) + ($padding * 2)

# Create Bitmap
$bmp = New-Object System.Drawing.Bitmap $width, $height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit

# Background
$bgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(30, 30, 30))
$g.FillRectangle($bgBrush, 0, 0, $width, $height)

# Title bar
$titleBarBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(45, 45, 48))
$g.FillRectangle($titleBarBrush, 0, 0, $width, $titleBarHeight)

# Terminal buttons (Close, Minimize, Maximize dots)
$redBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 95, 86))
$yellowBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 189, 46))
$greenBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(39, 201, 63))

$g.FillEllipse($redBrush, 20, 16, 13, 13)
$g.FillEllipse($yellowBrush, 40, 16, 13, 13)
$g.FillEllipse($greenBrush, 60, 16, 13, 13)

# Title text
$titleTextBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(200, 200, 200))
$g.DrawString("PowerShell - python recommendation_system.py", $titleFont, $titleTextBrush, 90, 13)

# Text lines
$y = $titleBarHeight + $padding
$defaultBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(220, 220, 220))
$cyanBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(86, 214, 230))
$greenTextBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(120, 220, 100))
$yellowTextBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(235, 203, 139))

foreach ($line in $lines) {
    $drawBrush = $defaultBrush
    if ($line -like "*WELCOME*" -or $line -like "*TOP *") {
        $drawBrush = $cyanBrush
    } elseif ($line -like "*[SUCCESS]*" -or $line -like "*[INFO]*") {
        $drawBrush = $greenTextBrush
    } elseif ($line -like "*---*") {
        $drawBrush = $yellowTextBrush
    }
    $g.DrawString($line, $font, $drawBrush, $padding, $y)
    $y += $lineHeight
}

# Save image
$outputPath = Join-Path (Get-Location) "execution_screenshot.png"
$bmp.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)

$g.Dispose()
$bmp.Dispose()

Write-Output "Screenshot saved successfully at: $outputPath"
