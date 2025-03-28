@echo off
echo ===== Jamboxx Infinite Build Script (Optimized) =====

REM 1. Clean and create output directory
if exist "dist" rmdir /s /q dist
mkdir dist

echo [1/3] Building application with Nuitka...
python -m nuitka --standalone ^
    --mingw64 ^
    --assume-yes-for-downloads ^
    --remove-output ^
    --include-package=app ^
    --include-package=app.core ^
    --include-package=app.ddsp ^
    --include-package=app.diffusion ^
    --include-package=app.encoder ^
    --include-package=app.enhancer ^
    --include-package=app.nsf_hifigan ^
    --include-package=app.routers ^
    --include-package=app.services ^
    --include-package=app.utils ^
    --include-package=app.config ^
    --include-package=fastapi ^
    --include-package=starlette ^
    --include-package=pydantic ^
    --include-package=transformers.models.hubert ^
    --include-package=transformers.models.wav2vec2 ^
    --include-module=torchcrepe ^
    --include-module=librosa ^
    --include-module=soundfile ^
    --include-module=demucs ^
    --include-module=unittest.mock ^
    --enable-plugin=multiprocessing ^
    --enable-plugin=numpy ^
    --enable-plugin=torch ^
    --enable-plugin=transformers ^
    --follow-imports ^
    --follow-import-to=fastapi ^
    --follow-import-to=uvicorn ^
    --show-progress ^
    --show-memory ^
    --warn-implicit-exceptions ^
    --warn-unusual-code ^
    --output-dir=dist ^
    --nofollow-import-to=matplotlib ^
    --nofollow-import-to=tkinter ^
    --enable-console ^
    app/main.py

echo [2/3] Copying additional resource files...
xcopy /E /I /Y ffmpeg dist\ffmpeg
xcopy /E /I /Y pretrain dist\pretrain
xcopy /E /I /Y app\config dist\app\config

echo [3/3] Verifying dependencies...
dist\main.exe --check-deps || (
    echo ERROR: Dependency check failed!
    exit /b 1
)

echo ===== Build Successful! =====
echo Executable: dist\main.exe
pause