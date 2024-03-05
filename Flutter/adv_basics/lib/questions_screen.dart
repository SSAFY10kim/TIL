import 'package:adv_basics/answer_button.dart';
import 'package:flutter/material.dart';

class QuestionsScreen extends StatefulWidget {
  const QuestionsScreen({super.key});

  @override
  State<QuestionsScreen> createState() => _QuestionScreenState();
}

class _QuestionScreenState extends State<QuestionsScreen> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            "The Questions...",
            style: TextStyle(
              color: Colors.white,
            ),
          ),
          const SizedBox(
            height: 30,
          ),
          AnserButton(anserText: "1", onTap: () {}),
          AnserButton(anserText: "2", onTap: () {}),
          AnserButton(anserText: "3", onTap: () {}),
          AnserButton(anserText: "4", onTap: () {})
        ],
      ),
    );
  }
}
