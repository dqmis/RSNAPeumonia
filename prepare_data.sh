if [ $1 == 'convert' ]
then
	echo Converting images
	python ./scripts/DICOM_convert.py
fi

echo Preparing data
python ./scripts/prepare_data.py
echo Moving images
python ./scripts/move_images.py
echo Preparing cfg for Darknet
python ./scripts/prepare_cfg.py
echo Preparing prediction file for Darknet
python ./scripts/prepare_pred.py

echo Done!
