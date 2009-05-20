%define name dekagen
%define version 1.0.2
%define release %mkrel 5

Summary:   Rips and encodes CD's
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
License:   GPLv2+
Group:     Sound
URL:       http://userpage.fu-berlin.de/~mbayer/tools/dekagen.html
Obsoletes: ripenc
Provides:  ripenc
Buildarch: noarch
BuildRequires: dos2unix

%description
The dekagen bourne shell script, formerly known as ripenc, is an interactive 
command line tool, that automates the whole process of ripping data from 
music compact discs (CD), the naming of the files, their converting 
into MP3 or Ogg-Vorbis format and the labelling of the MP3 files 
with an ID3 tag.

%prep
rm -rf $RPM_BUILD_ROOT

%setup 
#fix CRLF in CHANGES
cp --preserve CHANGES CHANGES.msdos
dos2unix -U CHANGES

%build

%install

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1

cp dekagen ${RPM_BUILD_ROOT}%{_bindir}
gunzip dekagen.1.gz
cp dekagen.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING CHANGES INSTALL CREDITS README
%_bindir/*
%_mandir/man1/*

