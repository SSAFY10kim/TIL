import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:testweb/webview_controller.dart.dart';

//main.dart
void main() {
// Flutter 애플리케이션의 위젯 바인딩을 초기화
  WidgetsFlutterBinding.ensureInitialized();

  // 반응형 상태 관리 controller 등록
  Get.put(WebviewMainController());
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    //WebviewMainController의 controller를 호출
    late final controller = WebviewMainController.to.getController();

    return MaterialApp(
      home: Scaffold(
        appBar: PreferredSize(
            //앱 바는 필요하지 않았기에 0으로
            preferredSize: const Size.fromHeight(0),
            // elevation = 필요하지 않은 그림자 효과
            child: AppBar(elevation: 0)),
        //WebViewWidget에 controller를 parameter로 넘겨준다
        body: WebViewWidget(controller: controller),
      ),
    );
  }
}
