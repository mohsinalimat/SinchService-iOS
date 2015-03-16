Pod::Spec.new do |s|

  s.name         = "SinchService"
  s.version      = "1.0.0"
  s.platform     = :ios, '6.0'

  s.summary      = "SinchService provides the class SINService which is a high-level wrapper around the Sinch iOS SDK"

  s.description  = <<-DESC
  SinchService provides the class SINService which is a high-level wrapper around the Sinch iOS SDK.
  DESC

  s.homepage     = "http://www.sinch.com"

  s.author       = { "Christoffer Ahlbin" => "christoffer@sinch.com" }

  s.license      = { :type => 'Apache' }

  s.source       = { :git => 'https://github.com/sinch/SinchService-iOS.git', :tag => '1.0.0' }
  s.public_header_files = 'SinchService/SINService.h,SinchService/SinchService.h'
  s.source_files = 'SinchService/*.{h,m}'

  # shim target for Sinch.framework headers so that #import <Sinch/Sinch.h> works
  s.subspec 'SinchHeaders' do |ss|
    ss.source_files = 'SinchService/PrivateHeaders/Sinch/*.h'
    ss.header_dir = 'Sinch'
  end

end
