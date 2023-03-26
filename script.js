
const recordButton = document.getElementById('record-btn');
const waveform = WaveSurfer.create({
    container: '#waveform',
    waveColor: 'black',
    progressColor: 'red'
});

let recorder = null;
let chunks = [];
let mediaStream = null;

recordButton.onclick = function () {
    if (!recorder) {
        navigator.mediaDevices.getUserMedia({audio: true})
            .then(function(stream) {
                mediaStream = stream;
                recorder = new RecordRTC(stream, {
                    type: 'audio',
                    mimeType: 'audio/wav',
                    timeSlice: 4000,
                    ondataavailable: function (data) {
                        chunks.push(data);
                    }
                });
                recorder.startRecording();
                waveform.microphone = mediaStream;
                waveform.recorder = recorder;
                waveform.empty();
                waveform.start();
                recordButton.innerHTML = 'Stop';
                setTimeout(stopRecording, 12000);
            })
            .catch(function(error) {
                console.log(error);
            });
    } else {
        stopRecording();
    }
};

function stopRecording() {
    if (recorder) {
        recorder.stopRecording(function() {
            mediaStream.getTracks().forEach(function(track) {
                track.stop();
            });
            waveform.stop();
            recordButton.innerHTML = 'Record';
            let blob = new Blob(chunks, {type: 'audio/wav'});
            let url = URL.createObjectURL(blob);
            let link = document.createElement('a');
            link.href = url;
            link.download = 'recording.wav';
            document.body.appendChild(link);
            link.click();
            chunks = [];
            recorder = null;
        });
    }
}
