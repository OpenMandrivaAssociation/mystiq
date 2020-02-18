%define oname MystiQ

Summary:	Audio/Video converter
Name:		mystiq
Version:	20.02.18
Release:	1
License:	GPLv3
Group:		Video
Url:		https://mystiq.swlx.info/
Source0:	https://github.com/llamaret/MystiQ/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(x11)

Requires:	ffmpeg
Requires:	sox

%description
MystiQ is a GUI for FFmpeg, a powerful media converter. 
FFmpeg can read audio and video files in various 
formats and convert them into other formats. 
MystiQ features an intuitive graphical 
interface and a rich set of presets to help you 
convert media files within a few clicks.
Advanced users can also adjust conversion parameters in detail.

%files
%doc LICENSE README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/mystiq.svg
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*.1.zst

#-----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
chmod -x mystiq.desktop icons/mystiq.svg

%build
qmake-qt5 mystiq.pro
make USE_LIBNOTIFY=1 -j3 VERBOSE=1

%install
%qmake5_install
