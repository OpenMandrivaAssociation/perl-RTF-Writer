%define realname   RTF-Writer
%define version    1.11
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    for generating documents in Rich Text Format
Source:     http://www.cpan.org/modules/by-module/RTF/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Path)
BuildRequires: perl(Image::Size)
BuildRequires: perl(UNIVERSAL)
BuildRequires: perl(strict)

BuildArch: noarch

%description
This module is for generating documents in Rich Text Format. 

This module is a class; an object belonging to this class acts like an
output filehandle, and calling methods on it causes RTF text to be written.

Incidentally, this module also exports a few useful functions, upon
request.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
