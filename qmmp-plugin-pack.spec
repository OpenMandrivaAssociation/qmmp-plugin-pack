%define oname qmmp
%define major %(echo %{version} |cut -d. -f1-2)

Summary:	A set of extra plug-ins for Qmmp
Name:		qmmp-plugin-pack
Version:	2.0.1
Release:	1
Group:		Sound
License:	GPLv2+
Url:		http://qmmp.ylsoftware.com/plugins.php
Source0:	http://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires: qt6-cmake
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
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(qmmp) >= %{version}
BuildRequires:	pkgconfig(qmmpui) >= %{version}
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires: pkgconfig(libxmp)
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
%{_libdir}/qmmp-%{major}/Input/libxmp.so
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

%build
# As of 1.5.0 can't compile with Clang, due to change in FFAP
# from changelog:
#" replaced assembler optimizations by GCC attributes in the ffap plugin"
#this cause this error at compiling: 
# /builddir/build/BUILD/qmmp-plugin-pack-1.5.0/src/Input/ffap/ffap.c:1257:1: error: function multiversioning is not supported on the current target
# DECLARE_SCALARPRODUCT_AND_MADD(c, "default")
export CC=gcc
export CXX=g++
%cmake
%make_build

%install
%make_install -C build
