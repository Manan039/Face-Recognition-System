
import t4 as t
faces,faceID=t.labels_for_training_data('trainingimages')
face_recognizer=t.train_classifier(faces,faceID)
face_recognizer.save('trainingData_frdt.yml')
name={0:"Bill Gates",1:"Mark Zuckerberg"}

