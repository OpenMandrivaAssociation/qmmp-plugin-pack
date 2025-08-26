%define oname qmmp
%define major %(echo %{version} |cut -d. -f1-2)

Summary:	A set of extra plug-ins for Qmmp
Name:		qmmp-plugin-pack
Version:	2.2.2
Release:	2
Group:		Sound
License:	GPLv2+
Url:		https://qmmp.ylsoftware.com/plugins.php
Source0:	https://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2
BuildRequires:	cmake ninja
BuildRequires:	qt6-cmake
BuildRequires:	yasm
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	qt6-qttools
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(opengl)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	vulkan-headers
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(qmmp) >= %{version}
BuildRequires:	pkgconfig(qmmpui) >= %{version}
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libxmp)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(zlib)
Recommends:	%{oname}-ffap = %{EVRD}
# Gone in 1.3.x
Obsoletes:	%{oname}-mpg123 < %{EVRD}


%description
Plug-ins for Qmmp from Qmmp Plug-in Pack:
 * FFap - enhanced Monkey's Audio (APE) decoder
   (24-bit samples and embedded cue support)
 * Simple Ui - simple user interface based on standard widgets set

%files
%{_libdir}/qmmp-%{major}/Visual/libgoom.so
%{_libdir}/qmmp-%{major}/Effect/libsrconverter.so
%{_libdir}/qmmp-%{major}/Engines/libffvideo.so
%{_libdir}/qmmp-%{major}/Transports/libytb.so
#{_libdir}/qmmp-%{major}/Input/libxmp.so
%{_datadir}/metainfo/qmmp-plugin-pack.appdata.xml

#----------------------------------------------------------------------------

%package -n %{oname}-ffap
Summary:	Qmmp FFap Input Plugin
Group:		Sound

%description -n %{oname}-ffap
This is the FFap Input Plugin for Qmmp (enhanced Monkey's Audio (APE) decoder,
24-bit samples and embedded cue support).

%files -n %{oname}-ffap
%doc AUTHORS COPYING ChangeLog.rus README README.RUS ChangeLog ChangeLog.svn
%{_libdir}/%{oname}-%{major}/Input/libffap.so

#----------------------------------------------------------------------------

%prep
%setup -q
# As of 2.0.1, clang 13.0.0,
# building with clang crashes at compile time
export CC=gcc
export CXX=g++
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
