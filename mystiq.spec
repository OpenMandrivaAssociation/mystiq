%define oname MystiQ

Summary:	Audio/Video converter
Name:		mystiq
Version:	20.02.18
Release:	15.1
License:	GPLv3
Group:		Video
Url:		https://mystiq.swlx.info/
Source0:	https://github.com/llamaret/MystiQ/archive/v%{version}.tar.gz
%if 0%{?is_opensuse}
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
%endif
%if 0%{?centos} || 0%{?fedora}
BuildRequires:  qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(x11)
%endif
%if 0%{?centos}


%endif
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
%{_mandir}/man1/*.1.xz

#-----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
chmod -x mystiq.desktop icons/mystiq.svg

%if 0%{?is_opensuse}
%build
qmake-qt5 mystiq.pro
make USE_LIBNOTIFY=1 -j3 VERBOSE=1
%endif

%if 0%{?centos} || 0%{?fedora}
qmake-qt5 mystiq.pro
make USE_LIBNOTIFY=1 -j3 VERBOSE=1
%endif

%if 0%{?is_opensuse} 
%install
%qmake5_install
%endif

%if 0%{?centos} || 0%{?fedora}
%install
%make_install INSTALL_ROOT=%{buildroot}
%endif

%if 0%{?is_opensuse}
%files
%defattr(-,root,root,-)
%doc LICENSE README.md CONTRIBUTING.md
%{_bindir}/mystiq
%{_datadir}/applications/mystiq.desktop
%{_datadir}/metainfo/mystiq.appdata.xml
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/mystiq.svg
%{_mandir}/man1/mystiq.1.gz
%endif

%if 0%{?centos} || 0%{?fedora}
%files
%doc LICENSE README.md CONTRIBUTING.md
%{_bindir}/mystiq
%{_datadir}/applications/mystiq.desktop
%{_datadir}/metainfo/mystiq.appdata.xml
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/mystiq.svg
%{_mandir}/man1/mystiq.1.gz
%endif
