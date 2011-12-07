Name: hunspell-mk
Summary: Macedonian hunspell dictionaries
%define upstreamid 20051126
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://mk.openoffice.org/files/documents/215/3053/mk_MK.zip
Group: Applications/Text
URL: http://mk.openoffice.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch
Patch0: hunspell-mk-iconv.patch

Requires: hunspell

%description
Macedonian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mk
#change encoding name to use the name that iconv knows this under
%patch0 -p1 -b .iconv.patch

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_mk_MK.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20051126-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20051126-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20051126-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 03 2008 Caolan McNamara <caolanm@redhat.com> - 0.20051126-1
- initial version
