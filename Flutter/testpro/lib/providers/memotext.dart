import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:testpro/providers/memo.dart';

class MemoText extends StatelessWidget {
  const MemoText({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    final TextEditingController textEditingController = TextEditingController();

    return Column(
      children: [
        Text(
          context.watch<Memo>().memo,
          style: const TextStyle(fontSize: 20),
        ),
        TextField(
          controller: textEditingController,
        ),
        ElevatedButton(
          onPressed: () {
            String newMemo = textEditingController.text;
            context.read<Memo>().setMemo(newMemo);
          },
          child: const Text('변경하기'),
        )
      ],
    );
  }
}
