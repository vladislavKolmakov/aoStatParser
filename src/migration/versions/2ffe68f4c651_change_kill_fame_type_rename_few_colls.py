"""change kill_fame type, rename few colls

Revision ID: 2ffe68f4c651
Revises: eb3c4e386685
Create Date: 2024-07-21 13:45:11.772934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ffe68f4c651'
down_revision: Union[str, None] = 'eb3c4e386685'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('ALTER TABLE player ALTER COLUMN kill_fame TYPE INTEGER USING kill_fame::integer')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('average_item_power', sa.Integer(), nullable=True))
    op.add_column('player', sa.Column('main_hand', sa.String(), nullable=True))
    op.alter_column('player', 'kill_fame',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.drop_column('player', 'average_itemPower')
    op.drop_column('player', 'main_Hand')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('main_Hand', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('player', sa.Column('average_itemPower', sa.INTEGER(), autoincrement=False, nullable=True))
    op.alter_column('player', 'kill_fame',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.drop_column('player', 'main_hand')
    op.drop_column('player', 'average_item_power')
    # ### end Alembic commands ###
