# check the ntebook fo rPOETYR
from model.model_service import ModelService
from loguru import logger


@logger.catch   # it will provude extra info if any problem occur
def main():
    logger.info("running the application")
    ml_svc = ModelService()
    ml_svc.load_model()  # load model now dont use the model name
    pred = ml_svc.predict([85, 2015, 2, 20, 1, 1, 0, 0, 1])
    # print(pred)
    logger.info(f"PREDICTION : {pred}")


if __name__ == "__main__":
    main()
