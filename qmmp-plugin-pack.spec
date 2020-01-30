%define oname qmmp
%define major %(echo %{version} |cut -d. -f1-2)

Summary:	A set of extra plug-ins for Qmmp
Name:		qmmp-plugin-pack
Version:	1.3.1
Release:	1
Group:		Sound
License:	GPLv2+
Url:		http://qmmp.ylsoftware.com/plugins.php
Source0:	http://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	yasm
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(qmmp) >= %{version}
BuildRequires:	pkgconfig(qmmpui) >= %{version}
BuildRequires:	pkgconfig(taglib)
Suggests:	%{oname}-ffap = %{EVRD}
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
%cmake_qt5
%make

%install
%makeinstall_std -C build
