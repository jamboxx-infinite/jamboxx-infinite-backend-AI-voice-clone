@echo off
echo ===== Jamboxx Infinite 构建脚本 =====

REM 创建输出目录
if not exist "dist" mkdir dist

echo 正在使用Nuitka打包应用程序...
python -m nuitka --standalone ^
    --include-package=app ^
    --include-package=app.core ^
    --include-package=app.ddsp ^
    --include-package=app.diffusion ^
    --include-package=app.encoder ^
    --include-package=app.nsf_hifigan ^
    --include-package=app.routers ^
    --include-package=app.schemas ^
    --include-package=app.services ^
    --include-package=app.utils ^
    --include-package=app.config ^
    --follow-imports ^
    --show-progress ^
    --windows-disable-console ^
    --output-dir=dist ^
    app/main.py

echo 正在复制必要的资源文件...
xcopy /E /I /Y ffmpeg dist\ffmpeg
xcopy /E /I /Y pretrain dist\pretrain
REM xcopy /E /I /Y static dist\static
xcopy /E /I /Y app\config dist\app\config

echo ===== 构建完成! =====
echo 可执行文件位于: dist\main.exe